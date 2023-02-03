from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis,produk,customer

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg','nama','stok','jenis_id','link_gbr']
    search_fields=['kodebrg','nama']
    list_filter=['jenis_id']
    list_per_page=5

class kolomProduk(admin.ModelAdmin):
    list_display = ['kode_produk', 'nama', 'tempat', 'berat', 'jumlah']
    search_fields = ['kode_produk', 'nama']
    list_filter = ('jumlah',)
    list_per_page = 3


class kolomCustomer(admin.ModelAdmin):
    list_display = ['nomor', 'nama', 'nama_barang','jumlah']
    search_fields = ['nomor', 'nama']
    list_filter = ('jumlah',)
    list_per_page = 3

admin.site.register(Barang,kolomBarang)
admin.site.register(Jenis)
admin.site.register(produk, kolomProduk)
admin.site.register(customer, kolomCustomer)
