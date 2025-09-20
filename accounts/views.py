from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout

# Create your views here.





def signup_view(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)  #Logs the user directly after the signup
            return redirect('home') #Redirects them to the home page
    else:
        form = UserCreationForm() #IF it is a GET request , then Django gives you a form to full up
   
    return render(request , 'signup.html' , {"form" : form})
    


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user:
            login(request , user)
            return redirect('home')
        
        else:
            return render(request , 'login.html' , {'error' : "Invalid Credentials!"})
        

    return render(request , 'login.html')




def logout_view(request):
    logout(request)
    return redirect('login')