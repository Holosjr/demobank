from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
# def login(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('bankapp:inside')
#         else:
#             messages.info(request,"Invalid credentials")
#             return redirect('credential:login')
#     return render(request,"login.html")
# def register(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password= request.POST['password']
#         cpassword= request.POST['password1']
#         if password== cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username's Taken")
#                 return redirect('credential:register')
#             else:
#                 user=User.objects.create_user(username=username,password=password,)
#                 user.save();
#                 return redirect('credential:login')
#
#         else:
#             messages.info(request,"password's not matching")
#             return redirect('credential:register')
#         return redirect('bankapp:inside')
#     return render(request,"register.html")
#
# def logout(request):
#     auth.logout(request)
#     return redirect('bankapp:home')





def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        cpassword= request.POST.get('password1',default=password)
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username's Taken")
                return redirect('credential:register')

            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                print("user created")
                return redirect('credential:login')

        else:
            messages.info(request, "password's not matching")
            return redirect('credential:register')
        return redirect('/')
    return render(request,"register.html")


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:inside')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('credential:login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('bankapp:home')

def back(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        return redirect('bankapp:inside')
    return redirect('bankapp:inside')

