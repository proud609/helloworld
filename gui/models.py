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