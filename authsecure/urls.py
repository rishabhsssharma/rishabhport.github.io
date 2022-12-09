from django.contrib import admin
from django.urls import path
from authsecure import views
from django.urls import include, re_path
urlpatterns = [
  
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_handle,name="login"),
    path('logout/',views.logout_handle,name="logout"),
    
]
