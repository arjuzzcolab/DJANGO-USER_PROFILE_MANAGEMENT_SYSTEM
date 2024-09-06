from django.shortcuts import render,redirect
from .forms import userdetailsForm,userprojectsForm
from .models import userProfile,userProject
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
            return redirect('login')
        else:
            messages.info('password mismatch')
            return redirect('regsiter')
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('show')
        else:
            messages.info(request,'provide correct details')
            return redirect('login')
    return render(request,'login.html')
       
def manage_profile(request):
    try:
        user_profile = userProfile.objects.get(user=request.user)
    except userProfile.DoesNotExist:
        user_profile=None

    if request.method == 'POST':
        form = userdetailsForm(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)   
            user_profile.user = request.user
            user_profile.save() 
    else:
        form = userdetailsForm(instance=user_profile)
    return render(request,'profiledetails.html',{'form':form,'user_profile':user_profile})

def manage_project(request):
    try:
        user_profile = userProfile.objects.get(user=request.user)
        user_project = userProject.objects.get(user=user_profile)
    except userProject.DoesNotExist:
        user_project=None
    except userProfile.DoesNotExist:
        user_project=None
        user_profile=None
        

    if request.method == 'POST':
        form = userprojectsForm(request.POST,request.FILES,instance=user_project)
        if form.is_valid():
            user_project = form.save(commit=False)   
            user_project.user = user_profile
            user_project.save() 
    else:
        form = userprojectsForm(instance=user_project)
    return render(request,'projectdetails.html',{'form':form,'user_project':user_project,'user_profile':user_profile})

def logout(request):
    auth.logout(request)
    return redirect('login')

def show(request):
    try:
        user_profile = userProfile.objects.get(user=request.user)
    except userProfile.DoesNotExist:
        user_profile = None
    return render(request,'index.html',{'user_profile':user_profile})





def show_portfolio(request):
    try:
        user_profile = userProfile.objects.get(user=request.user)
        user_project = userProject.objects.get(user=user_profile)
    except userProfile.DoesNotExist:
        user_profile = None
        user_project = None
    except userProject.DoesNotExist:
        user_project = None
    return render(request,'index_portfolio2.html',{'user_profile':user_profile,'user_project':user_project})
