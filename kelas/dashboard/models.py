from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self) :
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True, default='img/')
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis,on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return "{}.  {}".format(self.kodebrg,self.nama)

class produk(models.Model):
    kode_produk = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    tempat = models.CharField(max_length=120)
    berat = models.CharField(max_length=10)
    jumlah = models.IntegerField()

    def __str__(self):
        return self.nama

class customer(models.Model):
    nomor = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    nama_barang = models.CharField(max_length=120)
    jumlah = models.IntegerField()

    def __str__(self):
        return self.nama