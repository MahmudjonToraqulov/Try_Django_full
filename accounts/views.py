from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm( request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('/login/')
    context = {
        'form': form
    }
    return render(request,'accounts/register.html',context=context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login( request , user )
            return redirect('/')
    return render( request,'accounts/login.html',{} )


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render( request,'accounts/logout.html',{} )