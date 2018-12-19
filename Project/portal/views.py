from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from portal.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import *
from django_feedparser import *
from .feeds import *
from datetime import datetime
import feedparser
from django.contrib.auth.views import (
    login, logout,password_reset,password_reset_done,password_reset_confirm,
password_reset_complete
)
from .middleware import *
from .context_processors import *

def f(request):
    dic=feedparser.parse('http://127.0.0.1:8000/portal/archivefeed/')
    context = {'dic': dic.entries}
    return render(request, 'portal/f.html', context)

def enter_feed(request):
    st = TeacherPersonal.objects.filter(user__id=request.user.id)
    if not st[0].adminPos == 'None': ##Teacher
        context = rssfeed.objects.filter(user__id=request.user.id).order_by('-date')
        if request.method == 'POST':
            form = FeedForm(request.POST, request.FILES)
            cont = {'context': context, 'form': form}
            if form.is_valid():
                model_instance=form.save(commit=False)
                model_instance.user = request.user
                model_instance.date = datetime.now()
                model_instance.save()
                return redirect('/portal/enter_feed/')
            return render(request, 'portal/feed.html', cont)
        else:
            form = FeedForm()
            cont = {'context': context, 'form': form}
            return render(request, 'portal/feed.html', cont)
        return HttpResponse('Yo')
    else:
        return HttpResponse('Not authorized')
    
    
    
def view_t(request,uname):
    user = User.objects.get(username=uname)
    try:
        details = TeacherPersonal.objects.filter(user=user)
        args = {'context': details[0],
            'name':user,}
        return render(request, 'portal/view_t.html', args)
    except:
        return render(request, 'portal/no_det.html')


def view_s(request,uname):
    user = User.objects.get(username=uname)
    try:
        details = Personal.objects.filter(user=user)
        args = {'context': details[0],
            'name':user,}
        return render(request, 'portal/view_s.html', args)
    except:
        return render(request, 'portal/no_det.html')
        

def home(request):
    user = request.user
    
    if user.is_authenticated():
        if not user.has_usable_password():
            return redirect('/portal/setUsername')

            args = {'user': user, 'form':form}
            return render(request, 'portal/setUsername.html', args)

        try:
            profile = UserProfile.objects.get(user=user)
            if profile.status == "Student" and profile.program == '':
                return redirect('/portal/further_details')
            
            dic=feedparser.parse('http://127.0.0.1:8000/portal/archivefeed/')
            args = {'user': user, 'dic': dic.entries[:2]}
            #print(dic)
            return render(request, 'portal/home.html', args)
        except:
            return redirect('/portal/add_status')
            
    dic=feedparser.parse('http://127.0.0.1:8000/portal/archivefeed/')
    args = {'user': user, 'dic': dic.entries[:2]}
    #print(args)
    return render(request, 'portal/home.html', args)

def setUsername(request):
    if request.method == 'POST':
        form = SetUsername(request.POST)
        if form.is_valid():
            user = request.user
            post = request.POST
            
            user.set_password(post['password1'])
            user.username = post['username']
            user.save()
            return redirect('/portal/')
        return render(request, 'portal/setUsername.html', {'form': form})
    else:
        form = SetUsername()

        args = {'form': form}
        return render(request, 'portal/setUsername.html', args)


@login_required(login_url='/portal/login/')
def add_status(request):
    formname = "Status Form"
    if request.method == 'POST':
        form = StatusForm(request.POST)
        
        if form.is_valid():
            user = request.user
            profile = UserProfile.objects.create(user=request.user)
            
            post = request.POST
            status = post['status']
            dept = post['department']
            
            profile.status = status
            profile.department = dept
            profile.save()
            return redirect('/portal/')
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})
    else:
        form = StatusForm()
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})

@login_required(login_url='/portal/login/')
def further_details(request):
    formname = "Further Details"
    if request.method == 'POST':
        form = StudentStatus(request.POST)
        
        if form.is_valid():
            user = request.user
            profile = UserProfile.objects.get(user=user)
            
            post = request.POST
            program = post['program']
            year = post['year']
            
            profile.program = program
            profile.year = year
            profile.save()
            
            return redirect('/portal/')
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})
    else:
        form = StudentStatus()
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})




def see_t_list(request,dep):
    teachers = UserProfile.objects.filter(status='Teacher',department=dep).order_by('department')
    context = {
        'teachers': teachers,
    }
    return render(request, 'portal/t_list.html', context)



def see_s_list1(request,dep):
    context = {
            'dep': dep,
    }
    return render(request, 'portal/see_s_list1.html', context)

    
def see_s_list2(request,dep,prog):
    context = {
            'dep': dep,
            'prog':prog,
    }
    return render(request, 'portal/see_s_list2.html', context)

def see_s_list(request,dep,prog,year):
    students = UserProfile.objects.filter(status='Student',department=dep,program=prog,year=year)
    #print(students[1])
    context = {
        'students': students,
    }
    return render(request, 'portal/s_list.html', context)




@login_required(login_url='/portal/login/')
def t_reg_subject(request):
    formname = "Course Registration Form"
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            post = request.POST
            subject = post['subject']
            if subject == 'None' or subject == 'none':
                return render(request, 'portal/t_form_popup.html',  {'form': form, 'formname': formname})
            model_instance=form.save(commit=False)
            model_instance.user = request.user
            model_instance.save()
            return redirect('/portal/profile/')
        return render(request, 'portal/t_form_popup.html',  {'form': form, 'formname': formname})
    else:
        form = SubjectForm()
        return render(request, 'portal/t_form_popup.html',  {'form': form, 'formname': formname})




@login_required(login_url='/portal/login/')
def view_t_reg_subject(request):
    subjects = Subject.objects.filter(user__id=request.user.id)
    context = {
        'subjects': subjects,
    }
    return render(request, 'portal/t_reg_sub_list.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/portal/login/')
        return render(request, 'portal/reg_form.html', {'form': form})
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'portal/reg_form.html', args)




@login_required(login_url='/portal/login/')
def reg_subject(request):
    formname = "Course Registration Form"
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.user = request.user
            model_instance.save()
            return redirect('/portal/profile/')
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})
    else:
        form = CourseForm()
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})

@login_required(login_url='/portal/login/')
def view_reg_subject(request):
    try:
        course = Course.objects.filter(user__id=request.user.id)
        dep_ob = UserProfile.objects.get(user__id=request.user.id)
        dep = dep_ob.department
        prog = dep_ob.program
        year = dep_ob.year
        s1 = course[0].subject1
        s2 = course[0].subject2
        s3 = course[0].subject3
        s4 = course[0].subject4
        s5 = course[0].subject5
        t1 = {'first_name':'(No Teacher has been alloted so far!)'}
        t2 = {'first_name':'(No Teacher has been alloted so far!)'}
        t3 = {'first_name':'(No Teacher has been alloted so far!)'}
        t4 = {'first_name':'(No Teacher has been alloted so far!)'}
        t5 = {'first_name':'(No Teacher has been alloted so far!)'}
        if not s1=='None':
            t = Subject.objects.filter(subject=s1,department=dep, program=prog,year=year)
            if len(t)>0:
                t1 = t[0].user

        if not s2=='None':
            t = Subject.objects.filter(subject=s2,department=dep, program=prog,year=year)
            if len(t)>0:
                t2=t[0].user
            
        if not s3=='None':
            t = Subject.objects.filter(subject=s3,department=dep, program=prog,year=year)
            if len(t)>0:
                t3=t[0].user
                
        if not s4=='None':
            t = Subject.objects.filter(subject=s4,department=dep, program=prog,year=year)
            if len(t)>0:
                t4=t[0].user
        
        if not s5=='None':
            t = Subject.objects.filter(subject=s5,department=dep, program=prog,year=year)
            if len(t)>0:
                t5=t[0].user
    
        args = {'s1':s1, 's2':s2, 's3':s3, 's4':s4, 's5':s5, 't1':t1, 't2':t2, 't3':t3, 't4':t4, 't5':t5, 'user': request.user,}
        return render(request, 'portal/view_reg_subject.html', args)
    except:
        return redirect('/portal/reg_subject')

def edit_reg_sub(request):
    formname = "Edit Course Registration Details"
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=Course.objects.get(user__id=request.user.id))

        if form.is_valid():
            form.save()
            return redirect('/portal/view_reg_subject')
        return render(request, 'portal/edit_reg_sub.html', {'form': form, 'formname' : formname})
    else:
        form = EditCourseForm(instance=Course.objects.get(user__id=request.user.id))
        args = {'form': form, 'formname' : formname}
        return render(request, 'portal/edit_reg_sub.html', args)






@login_required(login_url='/portal/login/')
def view_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    args = {'user': user, 'profile' : profile}

    if profile.status == "Teacher":
        return render(request, 'portal/teacher_profile.html', args) 
    else:
        return render(request, 'portal/student_profile.html', args)







@login_required(login_url='/portal/login/')
def personal_details(request):
    formname = "Personal Details"
    if request.method == 'POST':
        form = PersonalForm(request.POST, request.FILES)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.user = request.user
            model_instance.save()
            return redirect('/portal/profile/')
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})
    else:
        form = PersonalForm()
        return render(request, 'portal/form_popup.html',  {'form': form, 'formname': formname})

@login_required(login_url='/portal/login/')
def view_personal_details(request):
    try:
        context = Personal.objects.filter(user__id=request.user.id)
        args = {'context': context[0], 'user': request.user}
        return render(request, 'portal/view_personal_details.html', args)
    except:
        return redirect('/portal/personal_details')

def edit_personal_details(request):
    formname = "Edit Personal Details"
    if request.method == 'POST':
        form = EditPersonalForm(request.POST, request.FILES, instance=Personal.objects.get(user__id=request.user.id))

        if form.is_valid():
            form.save()
            return redirect('/portal/view_personal_details')
        return render(request, 'portal/edit_reg_sub.html',  {'form': form, 'formname': formname})
    else:
        form = EditPersonalForm(instance=Personal.objects.get(user__id=request.user.id))
        args = {'form': form}
        return render(request, 'portal/edit_reg_sub.html',  {'form': form, 'formname': formname})


@login_required(login_url='/portal/login/')
def t_personal_details(request):
    formname = "Personal Details"
    if request.method == 'POST':
        form = TeacherPersonalForm(request.POST, request.FILES)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.user = request.user
            model_instance.save()
            return redirect('/portal/profile/')
        return render(request, 'portal/t_form_popup.html',  {'form': form, 'formname': formname})
    else:
        form = TeacherPersonalForm()
        return render(request, 'portal/t_form_popup.html',  {'form': form, 'formname': formname})

@login_required(login_url='/portal/login/')
def t_view_personal_details(request):
    try:
        context = TeacherPersonal.objects.filter(user__id=request.user.id)
        args = {'context': context[0], 'user': request.user}
        return render(request, 'portal/t_view_personal_details.html', args)
    except:
        return redirect('/portal/t_personal_details')

def t_edit_personal_details(request):
    formname = "Edit Personal Details"
    if request.method == 'POST':
        form = EditTeacherPersonalForm(request.POST, request.FILES, instance=TeacherPersonal.objects.get(user__id=request.user.id))

        if form.is_valid():
            form.save()
            return redirect('/portal/t_view_personal_details')
        return render(request, 'portal/t_edit.html',  {'form': form, 'formname': formname})
    else:
        form = EditTeacherPersonalForm(instance=TeacherPersonal.objects.get(user__id=request.user.id))
        args = {'form': form}
        return render(request, 'portal/t_edit.html',  {'form': form, 'formname': formname})






@login_required(login_url='/portal/login/')
def bank_details(request):
    formname = "Bank Details"
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.user = request.user
            model_instance.save()
            return redirect('/portal/profile/')
        return render(request, 'portal/form_popup.html', {'form': form, 'formname': formname})
    else:
        form = BankForm()
        return render(request, 'portal/form_popup.html', {'form': form, 'formname': formname})

@login_required(login_url='/portal/login/')
def view_bank_details(request):
    try:
        context = Bank.objects.get(user__id=request.user.id)
        args = {'context': context, 'user': request.user}
        return render(request, 'portal/view_bank_details.html', args)
    except:
        return redirect('/portal/bank_details')

def edit_bank_details(request):
    formname = "Edit Bank Details"
    if request.method == 'POST':
        form = EditBankForm(request.POST, instance=Bank.objects.get(user__id=request.user.id))

        if form.is_valid():
            form.save()
            return redirect('/portal/view_bank_details')
        return render(request, 'portal/edit_reg_sub.html', {'form': form, 'formname': formname})
    else:
        form = EditBankForm(instance=Bank.objects.get(user__id=request.user.id))
        args = {'form': form, 'formname': formname}
        return render(request, 'portal/edit_reg_sub.html', args)








@login_required(login_url='/portal/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
    
        if form.is_valid():
            user = request.user
            post = request.POST
            email = post['email']
            fname = post['first_name']
            lname = post['last_name']

            user.email = email
            user.first_name = fname
            user.last_name = lname

            user.save()
            return redirect('/portal/profile')
        return render(request, 'portal/edit_profile.html', {'form': form})
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'portal/edit_profile.html', args)








@login_required(login_url='/portal/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/portal/profile')
        else:
            return redirect('/portal/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args= {'form': form}
        return render(request, 'portal/change_password.html', args)
    
@login_required(login_url='/portal/login/')
def notification(request):
    st = UserProfile.objects.filter(user__id=request.user.id, status='Teacher')
    
    if len(st) == 1: ##Teacher
        context = Posts.objects.filter(user__id=request.user.id).order_by('-date')
        if request.method == 'POST':
            form = PostsForm(request.POST, request.FILES)
            cont = {'context': context, 'form': form}
            if form.is_valid():
                model_instance=form.save(commit=False)
                model_instance.user = request.user
                model_instance.date = datetime.now()
                model_instance.save()
                return redirect('/portal/notification/')
            return render(request, 'portal/t_notification.html', cont)
        else:
            form = PostsForm()
            cont = {'context': context, 'form': form}
            return render(request, 'portal/t_notification.html', cont)
    
    else: ##Student
        dep_ob = UserProfile.objects.filter(user__id=request.user.id)
        dep = dep_ob[0].department
        prog = dep_ob[0].program
        year = dep_ob[0].year
        context = Posts.objects.filter(department = dep, program = prog, year=year).order_by('-date')
        cont = {'context': context}
        return render(request, 'portal/s_notification.html', cont)
        
    
def sic(request,subject,dept,year,program):
    all_students_in_dept = UserProfile.objects.filter(status='Student', department=dept, year=year, program=program)
    l = []
    for student in all_students_in_dept:
        x = Course.objects.filter(user__id=student.user.id)
        if len(x) == 0:
            continue
        x=x[0]
        if x.subject1 == subject or x.subject2 == subject or x.subject3 == subject or x.subject4 == subject or x.subject5 == subject:
            l.append(x)
    return render(request, 'portal/sic.html', {'list': l})

            
   
@login_required(login_url='/portal/login/')
def deptChat(request):
    try:
        st = UserProfile.objects.get(user=request.user, status='Student')

        context = Chat.objects.filter(chatType='Department', department=st.department).order_by('-date')
        if request.method == 'POST':
            form = DeptChatForm(request.POST, request.FILES)
            cont = {'context': context, 'form': form}
            if form.is_valid():
                user = request.user

                model_instance=form.save(commit=False)
                model_instance.user = user
                model_instance.date = datetime.now()

                model_instance.chatType = 'Department'
                model_instance.department = user.userprofile.department

                model_instance.save()
                return redirect('/portal/deptChat/')
            return render(request, 'portal/deptChat.html', cont)
        else:
            form = DeptChatForm()
            cont = {'context': context, 'form': form}
            return render(request, 'portal/deptChat.html', cont)
    
    except:
        return redirect('/portal/profile')
   
@login_required(login_url='/portal/login/')
def classChat(request):
    try:
        st = UserProfile.objects.get(user=request.user, status='Student')

        context = Chat.objects.filter(chatType='Class', department=st.department, year=st.year).order_by('-date')
        if request.method == 'POST':
            form = ClassChatForm(request.POST, request.FILES)
            cont = {'context': context, 'form': form}
            if form.is_valid():
                user = request.user

                model_instance=form.save(commit=False)
                model_instance.user = user
                model_instance.date = datetime.now()

                model_instance.chatType = 'Class'
                model_instance.department = user.userprofile.department
                model_instance.year = user.userprofile.year

                model_instance.save()
                return redirect('/portal/classChat/')
            return render(request, 'portal/classChat.html', cont)
        else:
            form = ClassChatForm()
            cont = {'context': context, 'form': form}
            return render(request, 'portal/classChat.html', cont)
    
    except:
        return redirect('/portal/profile')


def manageAttendance(request):
    subjects = Subject.objects.filter(user__id=request.user.id)
    context = {
        'subjects': subjects,
    }
    return render(request, 'portal/manageAttendance.html', context)


def sicAttendance(request,subject,dept,year,program):
    subj = Subject.objects.get(user=request.user, subject=subject,department=dept,year=year,program=program)
    attendances = Attendance.objects.filter(subject=subj).order_by('date')

    all_students_in_dept = UserProfile.objects.filter(status='Student', department=dept,year=year,program=program)
    l = []
    percent = {}
    for student in all_students_in_dept:
        x = Course.objects.filter(user__id=student.user.id)
        if len(x) == 0:
            continue
        x=x[0]
        if x.subject1 == subject or x.subject2 == subject or x.subject3 == subject or x.subject4 == subject or x.subject5 == subject:
            l.append(x)
            percent[str(x.user.username)] = 0
    
    print(attendances)

    presents = []
    totalClasses = 0
    for att in attendances:
        currPre = []
        totalClasses += 1
        for st in att.present.all():
            currPre.append(str(st.user.username))
            percent[str(st.user.username)] += 1
        
        presents.append(currPre)
        print(att.present.all())
    for key in percent.keys():
        if totalClasses == 0:
            percent[key] = 0
        else:
            percent[key] = (percent[key]*100.0)/totalClasses
            percent[key] = round(percent[key], 2)
    print("presents")
    print(presents)
    print("percent")
    print(percent)

    return render(request, 'portal/sicAttendance.html', {'list': l, 'sub':subj, 'attendances':attendances, 'presents' : presents, 'percent' : percent, 'total' : totalClasses})

def addClass(request,subject,dept,year,program):
    all_students_in_dept = UserProfile.objects.filter(status='Student', department=dept,year=year,program=program)
    if request.method == 'GET':
        l = []
        for student in all_students_in_dept:
            x = Course.objects.filter(user__id=student.user.id)
            if len(x) == 0:
                continue
            x=x[0]
            if x.subject1 == subject or x.subject2 == subject or x.subject3 == subject or x.subject4 == subject or x.subject5 == subject:
                l.append(x)
        
        return render(request, 'portal/addClass.html', {'list': l})
    else:
        post = request.POST
        print(str(post))

        date = post['date']
        if not (date == ''):
            subj = Subject.objects.get(user=request.user, subject=subject,department=dept,year=year,program=program)
            try:
                att = Attendance.objects.get(subject=subj, date=date)
                return redirect('/portal/manageAttendance')
            except:
                att = Attendance.objects.create(subject=subj, date=date)

            for key in post.keys():
                if post[key] == 'on':
                    user = User.objects.get(username=str(key))
                    stud = UserProfile.objects.get(user=user)
                    att.present.add(stud)

            att.save()
        return redirect('/portal/manageAttendance')

def checkAttendance(request):
    user = request.user
    try:
        course = Course.objects.get(user__id=user.id)
    except:
        course = ''

    context = {
        'user' : user,
        'course': course,
    }
    return render(request, 'portal/checkAttendance.html', context)


def attendance(request,subject):
    user = request.user
    profile = UserProfile.objects.get(user__id=user.id)
    dep = profile.department
    prog = profile.program
    year = profile.year

    try:
        subj = Subject.objects.get(subject=subject,department=dep, program=prog,year=year)
        tAssigned = True
    except:
        tAssigned = False
        return render(request, 'portal/attendance.html', {'teacher' : tAssigned})
    teacher = subj.user
    attendances = Attendance.objects.filter(subject=subj).order_by('date')

    percent = 0
    dates = []
    totalClasses = 0
    present = 0

    for att in attendances:
        totalClasses += 1
        print(att.present.all())
        if profile in att.present.all():
            print("True")
            present += 1
            dates.append(att.date)
    
    print(dates)
    if not (totalClasses == 0):
        percent = round(((present*100.0)/totalClasses), 2)
    absent = totalClasses - present
    return render(request, 'portal/attendance.html', {'teacher' : tAssigned, 'total' : totalClasses, 'present' : present, 'absent' : absent, 'percent' : percent, 'attendances' : attendances, 'dates' : dates})
