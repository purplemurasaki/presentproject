from django.contrib import admin
from django.urls import path
from .views import loginview, homeview, listview, presentview, memorydetail,logoutview, messageview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginview, name='login'),
    path('home/', homeview, name='home'),
    path('list/', listview, name='list'),
    path('present/', presentview, name='present'),
    path('detail/<int:pk>/', memorydetail, name='detail'),
    path('logout/', logoutview, name='logout'),
    path('message/', messageview, name='message')
    ]
