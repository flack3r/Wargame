from django.conf.urls import url
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
    url(
        r'^accounts/login/',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(
        r'^accounts/logout/',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': '/blog/accounts/login'
        }
    ),
    url(r'^Register/', views.register, name='register'),
]
