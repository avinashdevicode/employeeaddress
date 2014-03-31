from django.db import models

# Create your models here.


class Address(models.Model):
    lat = models.CharField(max_length=70)
    lng = models.CharField(max_length=70)
    addres = models.CharField(max_length=550)
    dist = models.FloatField()
    
    def __unicode__(self):
        return ('%s,%s' % self.lat,self.lng)