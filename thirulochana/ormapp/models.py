from django.db import models
from django.contrib import admin
class product(models.Model):
    ProductID=models.CharField(primary_key=True,max_length=15)
    SI_NO=models.IntegerField()
    Product_Name=models.CharField(max_length=20)
    Description=models.CharField(max_length=60)
    Price=models.IntegerField()
    Weight=models.IntegerField()
    Stock_state=models.CharField(max_length=20)
class productAdmin(admin.ModelAdmin):
    list_display=["ProductID","SI_NO","Product_Name","Description","Price","Weight","Stock_state"]