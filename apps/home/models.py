# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from locale import currency
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pelanggan(models.Model):
    ID_pelanggan=models.CharField(max_length=200,primary_key=True)
    name=models.CharField('Nama Pelanggan',max_length=200)
    Regional=models.CharField('Regional',max_length=200)
    Segmen=models.CharField('Segmen Pelanggan', max_length=32, editable=False)
   

class Order(models.Model):
    ID_Order=models.CharField(max_length=200,primary_key=True)
    ID_pelanggan=models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    ID_Produk=models.CharField('Kode Produk',max_length=200)
    price=models.FloatField('Harga Produk')
    Currency=models.CharField(max_length=20)
    Quantity=models.FloatField()
    UoM=models.CharField('Unit of Measurement',max_length=200)
    Tanggal_Order=models.DateField()
    Tanggal_Pengiriman=models.DateField()
    Nilai_Order=models.CharField(max_length=32, editable=False)
    
    def save(self, *args, **kwargs):
        self.computed = self.Quantity + self.price
        super(Order, self).save(*args, **kwargs)