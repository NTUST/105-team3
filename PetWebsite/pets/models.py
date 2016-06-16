from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=20)
	gender = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	address=models.CharField(max_length=50)

	def __str__(self):
    		return self.name




class Pet(models.Model):
	
	name = models.CharField(max_length=20)
	age = models.CharField(max_length=15)
	gender = models.CharField(max_length=50, blank=True)
	sterilization = models.BooleanField(default=False)
	region=models.CharField(max_length=15,default='北部')
	health = models.CharField(max_length=50)
	other = models.CharField(max_length=100)
	pic_name=models.CharField(max_length=50,default='default.png')
	life_pic1=models.CharField(max_length=50,default='default.png')
	life_pic2=models.CharField(max_length=50,default='default.png')
	life_pic3=models.CharField(max_length=50,default='default.png')
	contact=models.ForeignKey(Contact)

	def __str__(self):
			return self.name