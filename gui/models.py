from django.db import models
from django.conf import settings

# Create your models here.
class Textmessage(models.Model):
    talker = models.CharField(max_length=30,blank = False)
    message = models.CharField(max_length=50,blank=True)
    talktime = models.CharField(max_length=50,blank=True)

    def _str_(self):
        return self.talker+ " "+self.message
    class Meta:
    	ordering = ['talktime']
class Resultcounter(models.Model):
	user = models.CharField(max_length=30,blank=False)
	counter = models.IntegerField()
	D_fire = models.BooleanField(default=False)
	D_blue = models.BooleanField(default=False)
	D_germ = models.BooleanField(default=False)
	D_moneyless = models.BooleanField(default=False)
	D_stone = models.BooleanField(default=False)
	D_sunburn = models.BooleanField(default=False)
	D_fight = models.BooleanField(default=False)
	D_sword = models.BooleanField(default=False)

	def _str_(self):
		return self.user+" "+self.message