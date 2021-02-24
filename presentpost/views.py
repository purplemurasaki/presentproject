from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import MemoryModel_1, PresentModel
from django.contrib.auth.decorators import login_required

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        # login画面でから送られたデータとUserテーブルのデータを照合する。
        user = authenticate(request, username=username_data,password=password_data)
        if user is not None:
            login(request, user)
            print(User.objects.all())
            return render(request, 'home.html')
            
        else:
            # redirectの目的はURLを遷移させること→処理をした後に遷移したいときに使う。
            return redirect('login')
            # renderの目的はhtmlとデータを用いて画面を描写すること。→処理と遷移を同時にしたいときに使う。
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('logout')

@login_required
def homeview(request):
    return render(request, 'home.html')
@login_required
def messageview(request):
    return render(request, 'message.html')

@login_required
def listview(request):
    object_list = MemoryModel_1.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


@login_required
def presentview(request):
    object_list = PresentModel.objects.all()
    return render(request, 'present.html', {'object_list': object_list})


@login_required
def memorydetail(request, pk):
    object = MemoryModel_1.objects.get(pk=pk)
    return render(request,'detail.html', {'object':object})


# Create your views here.
