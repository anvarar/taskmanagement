from django.contrib.auth import logout
from django.shortcuts import render,redirect
from .forms import loginform
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import addtask
from .models import add_details


# Create your views here.

#to perform signup 
def function1(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        try:
          form=User.objects.create_user(username,email,password)
          return redirect('login')
        except IntegrityError as e:
           return render(request,'signup.html',{'error':'username already exists'})
    else:
     form=loginform()
    return render(request,'signup.html',{'form':form})

#to perform login
def function2(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
          user = form.get_user()
          login(request, user)
          return redirect('home')
    else:
      form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#home page 
def homepage(request):
   return render(request,'home.html')

#add task
def add(request):
    if request.method=='POST':
      form=addtask(request.POST)
      #return render(request,'demo.html',{'form':form})
      if form.is_valid():
         form.save()
         print("DATA ENTERED SUCCESSFULLY") 
         return redirect('add')
    else:
     form=addtask()
    return render(request,'add.html',{'form':form})

#read task
def read(request):
    values=add_details.objects.all()
    return render(request,'read.html',{'values': values})

#delete task
def delete(request,id):
   value=add_details.objects.get(pk=id)
   value.delete()
   return redirect('read') 

#update task
def update(request,id):
    values=add_details.objects.get(pk=id)
    if request.method=='POST':
        form=addtask(request.POST,instance=values)
        if form.is_valid():
            form.save()
            return HttpResponse('data updated successfully')
    else:
        form=addtask(instance=values) 
    return render(request,'update.html',{'form':form})

#logout  
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    
    return render(request, 'login.html')