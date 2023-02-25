from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def homepage(request):
    return render(request,'page1.html')

def loginpage(request):
    return render(request,'page2.html')

def signuppage(request):
    return render(request,'page3.html')

def contactpage(request):
    
    if request.user.is_authenticated:
        return render(request,'page4.html')    
    return render(request,'page2.html')

#ForLogIn

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        if password==cpassword:  
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Already Exists, Try Another')
                
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password,
                    )
                user.save()
                print("Success")
        else:
            messages.info(request, 'Password doesnt match.')
            print("Please make sure your passwords match.") 
            return redirect('signuppage')   
        return redirect('user_login')
    else:
        return render(request,'page3.html')

def user_login(request):
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                
                if user is not None:
                    login(request,user)
                    auth.login(request, user)
                    messages.info(request, f'Welcome {username}')
                    return redirect('contactpage')
                else:
                    messages.info(request, 'Invalid username or password')
                    return redirect('loginpage')
            except:
                messages.info(request, 'Invalid username or password')
                return render(request, 'page2.html')
        else:
            
            return render(request, 'page2.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'page2.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('homepage')
