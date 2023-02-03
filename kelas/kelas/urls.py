
"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import *
def coba1(request):  
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'home.html')

def satu(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html')

def satus(request):
    titelnya="Produks"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produks.html')

def notif(request):
    titelnya="Notifikasi"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'notifikasi.html')

urlpatterns = [
 path('admin/', admin.site.urls),
 path('',coba1),
 path('produk/',Produk),
 path('produks/',satus),
 path('home/',coba1),
 path('addbarang/',tambah_barang), 
 path('customer/',Customer),
 path('notifikasi/',notif),
 path('VBrg/',Barang_View,name='VBrg'),
 path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
 path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
 ]
