# Generated by Django 2.2.12 on 2022-11-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='harga',
            new_name='jumlah',
        ),
        migrations.RenameField(
            model_name='produk',
            old_name='harga',
            new_name='jumlah',
        ),
    ]