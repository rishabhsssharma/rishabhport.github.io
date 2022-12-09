from django.contrib import admin
from django.urls import path
from portfolio import views
from django.urls import include, re_path
urlpatterns = [
  
    path('',views.home,name="home"),
    path('home/',views.home, name="home"),
    # path('login/',views.login,name="login"),
    # path('Signup/',views.Signup,name="Signup"),
    path('contact/',views.Contact,name="contact"),
    path('blog/',views.Bloghandle,name="Blog")
]
