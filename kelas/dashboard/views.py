from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang,produk,customer
from django.contrib import messages
from django.shortcuts import render,redirect

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil ditambahkan")
            form = FormBarang()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_barang.html',konteks)

    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs' : barangs
        }
    return render(request,'ubah_brg.html',konteks)

def Produk(request):
    Produks=produk.objects.all()
    konteks={
        'Produks':Produks,
    }
    return render(request,'produk.html',konteks)

def Customer(request):
    Customers=customer.objects.all()
    konteks={
        'Customers':Customers,
    }
    return render(request,'customer.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('VBrg')