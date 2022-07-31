from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . models import list1,card1
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
dic={'list1':list1,'card1':card1}
@never_cache
def home(request):
    if request.session.has_key('log'):
        return render(request,'home.html',dic)    
    else:
        return redirect('login')

def login(request):
    if request.session.has_key('log'):
        return redirect('home')
    else:
        if request.method =='POST':
            print('post')
            database={'username':'arshed','password':'12345'}
            username=request.POST['username']
            password=request.POST['password']
            if database['username']==username and database['password']==password:
                request.session['log'] = 'log'
                return redirect('home')
            else:
                messages.info(request, 'incorect email or password.')
                return redirect('login')
        else:
            return render(request,'login.html')


def logout(request):
    request.session.flush()
    return redirect('login')
        
