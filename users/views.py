from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Message
from django.contrib.auth.models import User
from .forms import CustomCreationForm,ProfileForm,SkillForm,MessageForm
from django.db.models import Q
from .utils import searchProfiles,paginationProfiles 
def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exists')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request,'Username or password is incorrect ')
    return render(request,'users/login_register.html')
def logoutUser(request):
    logout(request)
    messages.info(request,'User was logged out')
    return redirect('login')
def registerUser(request):
    page='register'
    form = CustomCreationForm()
    #context={'page':page,'form':form}
    if request.method == 'POST':
        form=CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account was created!')
            login(request,user)
            return redirect('edit-account')
        else:
            messages.error(request,'An error has occurred during registration')
    context={'page':page,'form':form}
    return render(request,'users/login_register.html',context)

def profiles(request):
    profiles,search_query=searchProfiles(request)
    custom_range,profiles=paginationProfiles(request,profiles,3)
    #profiles=Profile.objects.all()
    context={'profiles':profiles, 'search_query':search_query, 'custom_range':custom_range}
    return render(request, 'users/profiles.html',context)
def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topSkills=profile.skill_set.exclude(description__exact="")
    otherSkills=profile.skill_set.filter(description="")
    context={'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)

@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    skills=profile.skill_set.all()
    projects=profile.project_set.all()
    context={'profile':profile,'skills':skills,'projects':projects}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request,'users/profile_form.html',context)
@login_required(login_url='login')
def createSkill(request):
    profile=request.user.profile
    form=SkillForm()
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            messages.success(request,'Skill was added successfully!')
            return redirect('account')
    context={'form':form}

    return render(request,'users/skill_form.html',context)
@login_required(login_url='login')
def updateSkill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)
    if request.method=='POST':
        form=SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'Skill was added successfully!')
            return redirect('account')
    context={'form':form}

    return render(request,'users/skill_form.html',context)
@login_required(login_url='login')
def deleteSkill(request,pk):
    profile = request.user.profile
    skill=profile.skill_set.get(id=pk)
    if request.method=='POST':
        skill.delete()
        messages.success(request,'Skill was deleted successfully!')
        return redirect('account')
    context={'object':skill}
    
    return render(request,'delete_template.html',context)
@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    context={'messageRequest':messageRequest,'unreadCount':unreadCount}
    return render(request,'users/inbox.html',context)
@login_required(login_url='login')
def inboxMessage(request,pk):
    profile=request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read=True
        message.save()
    context={'message':message}
    return render (request,'users/message.html',context)

def createMessage(request,pk):
    recipient=Profile.objects.get(id=pk)
    form=MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('user-profile',pk=recipient.id)

    context={'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)
