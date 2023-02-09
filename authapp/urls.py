from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('attendance',views.attendance,name="attendance"),
    path('about',views.about,name="About"),
    path('send',views.send,name="send"),
]
