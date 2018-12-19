from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import "form model name"
from .models import *


class FeedForm(ModelForm):
    
    class Meta:
        model = rssfeed
        fields = ('title',
                  'msg',
        )
        
        
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class SetUsername(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2'
        )

class EditProfileForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
        
class StatusForm(ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('status', 'department')
        
class StudentStatus(ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('program', 'year')
        
class SubjectForm(ModelForm):
    
    class Meta:
        model = Subject
        fields = ('subject','program','department','year',)
        
        
class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ('subject1', 'subject2', 'subject3', 'subject4', 'subject5')
        
class EditCourseForm(ModelForm):
    
    class Meta:
        model = Course
        fields = ('subject1', 'subject2', 'subject3', 'subject4', 'subject5')
        exclude = ()

class BankForm(ModelForm):

    class Meta:
        model = Bank
        fields = ('BankName', 'BankBranch', 'AccountNo', 'IFSCode')
        
class EditBankForm(ModelForm):
    
    class Meta:
        model = Bank
        fields = ('BankName', 'BankBranch', 'AccountNo', 'IFSCode', )
        exclude = ()

class PersonalForm(ModelForm):

    class Meta:
        model = Personal
        fields = ('Contact', 'PermAddress', 'City', 'State','image', )
        
class EditPersonalForm(ModelForm):
    
    class Meta:
        model = Personal
        fields = ('Contact', 'PermAddress', 'City', 'State', 'image')
        exclude = ()

class TeacherPersonalForm(ModelForm):

    class Meta:
        model = TeacherPersonal
        fields = ('designation', 'adminPos', 'interest', 'Contact','image', )
        
class EditTeacherPersonalForm(ModelForm):
    
    class Meta:
        model = TeacherPersonal
        fields = ('designation', 'adminPos', 'interest', 'Contact','image', )
        exclude = ()

class PostsForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)
        self.fields['Notification'].required = True
    
    class Meta:
        model = Posts
        fields = ('Notification','program', 'department','year', 'file', )

class DeptChatForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(DeptChatForm, self).__init__(*args, **kwargs)
        self.fields['message'].required = True
    
    class Meta:
        model = Chat
        fields = ('message', 'file', )

class ClassChatForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ClassChatForm, self).__init__(*args, **kwargs)
        self.fields['message'].required = True
    
    class Meta:
        model = Chat
        fields = ('message', 'file', )



