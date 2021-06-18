from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from .forms import ContactForm, SignupForm,LoginForm,PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login
from .models import Post,Contact
from django.contrib.auth.models import Group

# Create your views here.

def Home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{
        "posts":posts
    })



class About(TemplateView):
    template_name="blog/about.html"

# class Contact(FormView):
#     form_class=ContactForm
#     template_name="blog/contact-us.html"
#     success_url="/contactpage"

def Contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data['user_name']
            uemail=form.cleaned_data['user_email']
            uaddress=form.cleaned_data['user_address']
            umsg=form.cleaned_data['user_msg']
            messages.success(request,'You Msg has been Sent')
            
                
    else:
        form=ContactForm()

        # messages.success(request,'You Email has been sent to the admin')
    return render(request,'blog/contact-us.html',{
        'form':form
            
    })





def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render(request,"blog/dashboard.html",{
            'posts':posts
        })
    else:
        return HttpResponseRedirect('/login')
    

def user_logout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,"You become an Author")
            form.save()
            # group=Group.objects.get(name="author")
            # user.group.add(group)
    else:
        form=SignupForm()
    return render(request,"blog/sign-up.html",{
        "form":form
    })

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In')
                    return HttpResponseRedirect('/dashboard')
            else:
                messages.warning(request,'Please check your username And password')
        else:
            form=LoginForm()
            
        return render(request,"blog/login.html",{
            "form":form
        })
    else :
        return HttpResponseRedirect('/dashboard')

def AddPost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                # pst.save()
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request,'blog/addpost.html',{
            'form':form
        })

def UpdatePost(request,id):

    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)

        return render(request,'blog/edit.html',{
                       'form':form
        })
    else:
        return HttpResponseRedirect('/login')

def DeletPost(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard')
        else:
            return HttpResponseRedirect('/login')
