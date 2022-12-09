from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import contact,Blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")



def Contact(request):
    if request.method == "POST":
        get_name = request.POST.get('name')
        get_email= request.POST.get('email')
        get_subject = request.POST.get('subject')
        get_message= request.POST.get('message_1')

        query = contact(name=get_name,email=get_email,subject=get_subject,message=get_message)
        query.save()
        messages.success(request,"Thanks for contacting")
        return redirect('/')


    return render(request,"contact.html")

def Bloghandle(request):

    posts=Blog.objects.all()
    context = {"posts":posts}
    return render(request,"handleblog.html",context)