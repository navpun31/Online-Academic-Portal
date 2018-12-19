from django.conf.urls import url, include
from . import views
from django_feedparser import *
from .feeds import *
from .feeds import *
from django.contrib.auth.views import (
    login, logout,password_reset,password_reset_done,password_reset_confirm,
password_reset_complete
)


urlpatterns=[
    url(r'^$', views.home),
    url(r'^register/$', views.register, name='register'),
    url(r'^setUsername/$', views.setUsername, name='setUsername'),
    url(r'^login/$', login, {'template_name': 'portal/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'portal/logout.html'}),
    url(r'^add_status/$', views.add_status, name='add_status'),
    url(r'^further_details/$', views.further_details, name='further_details'),
    url(r'^see_t_list/(?P<dep>[\w|\W]+)$', views.see_t_list, name='see_t_list'),
    url(r'^see_s_list/(?P<dep>[\w|\W]+)$', views.see_s_list1, name='see_s_list1'),
    url(r'^s_list/(?P<dep>[\w|\W]+)/(?P<prog>[\w|\W]+)$', views.see_s_list2, name='see_s_list2'),
    url(r'^see_s_list1/(?P<dep>[\w|\W]+)/(?P<prog>[\w|\W]+)/(?P<year>[\w|\W]+)$', views.see_s_list, name='see_s_list'),
    url(r'^archiveview/$', views.f,name='f'),
    url(r'^archivefeed/$', ArchiveFeed()),
    url(r'^enter_feed/$', views.enter_feed, name='enter_feed'),
    
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^reg_subject/$', views.reg_subject, name='reg_subject'),
    url(r'^t_reg_subject/$', views.t_reg_subject, name='t_reg_subject'),
    url(r'^view_t_reg_subject/$', views.view_t_reg_subject, name='view_t_reg_subject'),
    url(r'^view_reg_subject/$', views.view_reg_subject, name='view_reg_subject'),
    url(r'^edit_reg_sub/$', views.edit_reg_sub, name='edit_reg_sub'),
    url(r'^personal_details/$', views.personal_details, name='personal_details'),
    url(r'^view_personal_details/$', views.view_personal_details, name='view_personal_details'),
    url(r'^edit_personal_details/$', views.edit_personal_details, name='edit_personal_details'),
    url(r'^t_personal_details/$', views.t_personal_details, name='personal_details'),
    url(r'^t_view_personal_details/$', views.t_view_personal_details, name='view_personal_details'),
    url(r'^t_edit_personal_details/$', views.t_edit_personal_details, name='edit_personal_details'),
    url(r'^bank_details/$', views.bank_details, name='bank_details'),
    url(r'^edit_bank_details/$', views.edit_bank_details, name='edit_bank_details'),
    url(r'^view_bank_details/$', views.view_bank_details, name='view_bank_details'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$',password_reset,name='reset_password'),
    url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete'),

    url(r'^notification/$', views.notification, name='notification'),
    url(r'^deptChat/$', views.deptChat, name='deptChat'),
    url(r'^classChat/$', views.classChat, name='classChat'),

    url(r'^manageAttendance/$', views.manageAttendance, name='manageAttendance'),
    url(r'^manageAttendance/(?P<subject>[\w|\W]+)/(?P<dept>[\w|\W]+)/(?P<year>[\w|\W]+)/(?P<program>[\w|\W]+)$', views.sicAttendance, name='sicAttendance'),
    url(r'^addClass/(?P<subject>[\w|\W]+)/(?P<dept>[\w|\W]+)/(?P<year>[\w|\W]+)/(?P<program>[\w|\W]+)$', views.addClass, name='addClass'),
    url(r'^checkAttendance/$', views.checkAttendance, name='checkAttendance'),
    url(r'^checkAttendance/(?P<subject>[\w|\W]+)/$', views.attendance, name='attendance'),

    url(r'^(?P<subject>[\w|\W]+)/(?P<dept>[\w|\W]+)/(?P<year>[\w|\W]+)/(?P<program>[\w|\W]+)$', views.sic, name='sic'),
    url(r'^t/(?P<uname>[\w|\W]+)$', views.view_t, name='view_t'),
    url(r'^s/(?P<uname>[\w|\W]+)$', views.view_s, name='view_s'),
]


