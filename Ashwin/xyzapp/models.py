
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

