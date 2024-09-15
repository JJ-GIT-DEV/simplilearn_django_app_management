from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import UserInfo
from .forms import UserInfoAddForm  

# Create your views here.

def home(request):
    """
        Start page with to button for register(add-page) and check(fetch-page)
    """
    return render(request, "commeninfo/home.html", {})

def add(request):
    """
        Register page and new user to the database
        Before the data is saved in the database, a check\validation is carried out...
        username: muss unique and not None
        uniqueID: muss unique 
        password and password_re_trye: must equal and not None
    """
    submitted = False
    if request.method == "POST":
        form = UserInfoAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/commeninfo/add?submitted=True')
    else:
        form = UserInfoAddForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "commeninfo/add.html", {'form': form, 'submitted': submitted})

def fetch(request):
    """
        Check page for input uniqueID to check if user are registered
    """
    if request.method == "POST":
        #form = UserInfoCheckForm
        searched = request.POST.get('q')
        userinfos = UserInfo.objects.filter(uniqueID__icontains=searched)
        return render(request, "commeninfo/fetch.html", {'searched': searched, 'userinfos': userinfos})
    else:
        return render(request, "commeninfo/fetch.html", {})

def all_users(request):
    """
        Page print all users are registered with usernam, date of birth, uniqueID
    """
    user_list = UserInfo.objects.all()
    return render(request, "commeninfo/all_users.html", {'user_list': user_list})

#def search_users(request):
#    user_list = UserInfo.objects.all()
#    return render(request, "commeninfo/search_users.html", {'userinfo': user_list})