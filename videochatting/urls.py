from django.contrib import admin
from django.urls import path
from videochatting import views

urlpatterns = [
        path('',views.signup, name='home'),
        path('home',views.home, name='home'),
        path('about',views.about, name='about'),
        #path('services',views.services, name='services'),
        path('contact',views.contact, name='contact'),
        path('signin',views.signin, name='signin'),
        path('signup',views.signup, name='signup'),
        path('newmeeting',views.newmeeting, name='newmeeting'),
        path('logout',views.logout, name='logout'),
        path('leavemeeting',views.leavemeeting, name='leavemeeting'),
        #path('joinmeeting',views.joinmeeting, name='joinmeeting'),
        

]
