# Generated by Django 2.2.12 on 2022-11-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20221101_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_produk', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=100)),
                ('tempat', models.CharField(max_length=120)),
                ('berat', models.CharField(max_length=10)),
                ('harga', models.IntegerField()),
            ],
        ),
    ]