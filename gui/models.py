from django.db import models
from django.conf import settings

# Create your models here.
class Textmessage(models.Model):
	talker = models.CharField(max_length=30,blank = False)
	message = models.CharField(max_length=50,blank=True)
	def _str_(self):
		return self.talker + " "+ self.message

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)
    
class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField()
    restaurant = models.ForeignKey('Restaurant',  on_delete=models.CASCADE,)
