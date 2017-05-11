from django.conf.urls import url
from django.contrib.auth import views as auth_views
from MainApp import views
from MainApp.forms import LoginForm

urlpatterns = [
    url(r'^\Z', views.index, name='index'),
	url(r'guide/', views.guide, name='guide'),
	url(r'Dashboard/', views.Dashboard, name='dashboard'),
	url(r'problems/', views.problems, name='problems'),
	url(r'Tip/', views.Tip, name='Tip'),
	url(r'schedule/', views.schedule, name='schedule'),
    url(r'logout/', auth_views.logout, name = 'logout', kwargs={'next_page': '/'}),
    url(r'alert/', views.alert, name='alert'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'Web/', views.web, name='web'),
    url(r'Crypto/', views.crypto, name='crypto'),
    url(r'Reversing/', views.reversing, name='reversing'),
    url(r'Pwnable/', views.pwnable, name='pwnable'),
    url(r'Forensic/', views.forensic , name='forensic'),
    url(r'flagCheck/', views.flagCheck, name='flagCheck'),
    url(r'Rank/$', views.Rank, name='rank'),
    url(r'Rank/(?P<userid>.*)/$', views.Getdone),
    url(r'Profile/', views.Profile, name='profile'),
]
