# Ex01 Django ORM Web Application
## Date: 31.1.2026

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class zeptoDB(models.Model):
	Address=models.CharField(max_length=1000)
	Name=models.CharField(max_length=10)
	offers=models.CharField(max_length=100)
	Address2=models.CharField(max_length=100)
	feedback=models.CharField()
	Email=models.EmailField()
	Mobile_no=models.IntegerField(primary_key=True)
class zeptoDBAdmin(admin.ModelAdmin):
      list_display=['Address','Name','offers','Address2','feedback','Email','Mobile_no'];
admin.py
from django.contrib import admin
from .models import zeptoDB,zeptoDBAdmin
admin.site.register(zeptoDB,zeptoDBAdmin)
```



## OUTPUT

![alt text](<Screenshot (17).png>)

## RESULT
Thus the program for creating online food Delivery  website database using ORM has been executed successfully
