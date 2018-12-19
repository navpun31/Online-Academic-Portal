from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
from django.forms import ModelForm
from django_feedparser import *
# Create your models here.

statusch = [('Teacher','Teacher'),
          ('Student','Student')]

years = [('I','I'),
         ('II','II'),
         ('III','III'),
         ('IV','IV'),
         ('V','V')]

progs = [('B.Tech','B.Tech'),
           ('M.Tech','M.Tech'),
           ('IDD','IDD'),
           ('PHD','PHD'),]

deptch = [('Ceramic Engineering','Ceramic Engineering'),
          ('Computer Science and Engineering','Computer Science and Engineering'),
          ('Civil Engineering','Civil Engineering'),
          ('Electrical Engineering','Electrical Engineering'),
          ('Electronics Engineering','Electronics Engineering'),
          ('Mechanical Engineering','Mechanical Engineering'),
          ('Metallurgical Engineering','Metallurgical Engineering'),
          ('Mining Engineering','Mining Engineering'),
          ('Chemical Engineering','Chemical Engineering'),
          ('Pharmaceutical Engineering','Pharmaceutical Engineering'),
          ('Material Science and Technology','Material Science and Technology'),
          ('Biochemical Engineering','Biochemical Engineering'),
          ('Biomedical Engineering','Biomedical Engineering'),
          ('Department of Chemistry','Department of Chemistry'),
          ('Department of Physics','Department of Physics'),
          ('Department of Mathematical Sciences','Department of Mathematical Sciences')]

subjects=[
    ('None', 'None'),
    ('MA202: Statistics and Probability','MA202: Statistics and Probability'),
    ('CSO211: Computer System Organization','CSO211: Computer System Organization'),
    ('CSO204: Discrete Maths','CSO204: Discrete Maths'),
    ('ME104: Engineering Mechanics','ME104: Engineering Mechanics'),
    ('H105: Philosophy','H105: Philosophy'),
    ('MA101: Engineering Mathematics-I','MA101: Engineering Mathematics-I'),
    ('MA102: Engineering Mathematics-II','MA102: Engineering Mathematics-II'),
    ('CSO101: Introduction to Computer Programming','CSO101: Introduction to Computer Programming'),
    ('CSO102: Data Structures','CSO102: Data Structures'),
    ('EO101: Fundamentals of Electrical Engineering','EO101: Fundamentals of Electrical Engineering'),
    ('PHY101: Physics - Classical, Quantum and Relativistic','PHY101: Physics - Classical, Quantum and Relativistic'),
    ('PHY102: Physics - Electrodynamics','PHY102: Physics - Electrodynamics'),
    ('CY101: Chemistry','CY101: Chemistry'),
    ('CSE105: Information Technology Workshop-I','CSE105: Information Technology Workshop-I'),
    ('CSE205: Information Technology Workshop-II','CSE205: Information Technology Workshop-II'),
    ('H104: History and Civilization','H104: History and Civilization'),
    ('H103: Education and Self','H103: Education and Self'),
    ('H102: Development of Societies','H102: Development of Societies'),
    ('H101: Universal Human Values','H101: Universal Human Values')
]

chats = [
  ('Department','Department'),
  ('Class','Class')
]

designation = [
  ('Associate Professor', 'Associate Professor'),
  ('Assistant Professor', 'Assistant Professor'),
  ('Professor', 'Professor'),
]

administrative = [
  ('None','None'),
  ('Director', 'Director'),
  ('Dean of Academic Affairs', 'Dean of Academic Affairs'),
  ('Associate Dean of Academic Affairs', 'Associate Dean of Academic Affairs'),
  ('Dean of Student Affairs', 'Dean of Student Affairs'),
  ('Dean of Resource and Alumni', 'Dean of Resource and Alumni'),
  ('Dean of Research and Development', 'Dean of Research and Development'),
  ('Registrar', 'Registrar'),
  ('Professor Incharge(Faculty Affairs)', 'Professor Incharge(Faculty Affairs)'),
]


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,default='None', choices=subjects)
    program = models.CharField(max_length=100, null=True,default='B.Tech', choices=progs)
    department = models.CharField(max_length=100, null=True,default='Ceramic Engineering', choices=deptch)
    year = models.CharField(max_length=50, null=True,default='I',choices=years)
    
    def __str__(self):
        return ('%s %s - %s - %s %s Part %s ') %(self.user.first_name, self.user.last_name, self.subject, self.program, self.department, self.year)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject1= models.CharField('Subject 1',max_length=100,default='None', choices=subjects)
    subject2= models.CharField('Subject 2',max_length=100,default='None', choices=subjects)
    subject3= models.CharField('Subject 3',max_length=100,default='None', choices=subjects)
    subject4= models.CharField('Subject 4',max_length=100,default='None', choices=subjects)
    subject5= models.CharField('Subject 5',max_length=100,default='None', choices=subjects)
        
    def __str__(self):
        return ('%s') %(self.user.username)


class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    BankName = models.CharField('Bank Name', default='',max_length=100)
    BankBranch = models.CharField('Bank Branch', default='',max_length=100)
    AccountNo = models.CharField('Account Number',default='',max_length=100)
    IFSCode = models.CharField(default='',max_length=100)
        
    def __str__(self):
        return self.user.username

class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Contact = models.CharField(max_length=100)
    PermAddress= models.CharField('Permanent Address',max_length=100)
    City= models.CharField(max_length=100)
    State= models.CharField(max_length=100)
    image = models.FileField('Profile Image',null=True, blank=True)
        
    def __str__(self):
        return self.user.username

class TeacherPersonal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=100, null=True,default='B.Tech', choices=designation)
    adminPos = models.CharField('Administrative Position',max_length=100, null=True,default='Ceramic Engineering', choices=administrative)
    interest = models.CharField('Area(s) of Interest',max_length=200)

    Contact = models.CharField(max_length=100)
    image = models.FileField('Profile Image', null=True, blank=True)
        
    def __str__(self):
        return '%s - %s' %(self.user.username, self.Contact)
    
class rssfeed(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField('Title',max_length=100,default='')
    msg = models.CharField('Message',max_length=300,default='')
    date = models.DateTimeField()
    
    def __str__(self):
        return self.user.username

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    Notification = models.CharField(max_length=300,default='')
    
    program = models.CharField(max_length=100, null=True,default='B.Tech', choices=progs)
    department = models.CharField(max_length=100, null=True,default='Ceramic Engineering', choices=deptch)
    year = models.CharField(max_length=50, null=True,default='I',choices=years)
    
    date = models.DateTimeField()
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return '%s - %s' %(self.user.username, self.Notification)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    chatType = models.CharField(max_length=100, null=True,default='Class', choices=chats)
    message = models.CharField(max_length=300,default='')
    
    department = models.CharField(max_length=100, null=True,default='Ceramic Engineering', choices=deptch)
    year = models.CharField(max_length=50, null=True,default='I',choices=years)
    
    date = models.DateTimeField()
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return '%s - %s - %s - %s' %(self.user.username, self.department, self.year, self.message)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    status = models.CharField(max_length=100,default='Student', choices=statusch)
    program = models.CharField(max_length=100, null=True,default='', choices=progs)
    department = models.CharField(max_length=100, null=True,default='Ceramic Engineering', choices=deptch)
    year = models.CharField(max_length=50, null=True,default='I',choices=years)
    
    def __str__(self):
        return str(self.user.username)
    

class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.ManyToManyField(UserProfile, null=True)

    def __str__(self):
        return ('%s  ----  %s ---- PRESENT - %s') %(self.subject, self.date, " - ".join([s.user.username for s in self.present.all()]))

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        UserProfile.objects.create(user=kwargs['instance'])
#
#post_save.connect(create_profile, sender=User)