from django.shortcuts import render, HttpResponseRedirect
from project.forms import Patient,Login

from project.models import OurPatient

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Signup View Function
def sign_up(request):
 if request.method == "POST":
 
  xy = Patient(request.POST,request.FILES)
  if xy.is_valid():
   messages.success(request, 'Account Created Successfully !!') 
   xy.save()
 else: 
 
   xy =Patient()
 return render(request, 'enroll/signup.html', { 'form1':xy})


# Login View Function
# def user_login(request):
#   if not request.user.is_authenticated:
#     if request.method == "POST":
#       fm = Patient(request=request, data=request.POST)
#       if fm.is_valid():
#         uname = fm.cleaned_data['username']
#         upass = fm.cleaned_data['password']
#         user = authenticate(username=uname, password=upass)
#         if user is not None:
#           login(request, user)
#           messages.success(request, 'Logged in successfully !!')
#           return HttpResponseRedirect('/profile/')
#     else: 
#       fm = AuthenticationForm()
#     return render(request, 'enroll/userlogin.html', {'form':fm})
#   else:
#     return HttpResponseRedirect('/profile/')

def user_login(request):
       if request.method=='POST':
              cm=Login(request.POST)
              if cm.is_valid():
                     nm=cm.cleaned_data['Username']
                     tt=cm.cleaned_data['Password']
                     sm=OurPatient.objects.filter(username=nm,password=tt)
                   
                     return render(request,'enroll/profile.html',{'fight':sm})
       else:

             cm=Login()
       return render(request,'enroll/maha.html',{'form':cm})

# Profile
def user_profile(request):
  if request.user.is_authenticated:
    return render(request, 'enroll/profile.html', {'name': request.user})
  else:
    return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')