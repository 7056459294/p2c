from django.db import models #p2c-21-085


class Events(models.Model):   #p2c-21-085
    events_name = models.CharField(max_length=500) #p2c-21-085
    event_organizer = models.CharField(max_length=100) #p2c-21-085
    organizer_contact = models.IntegerField(blank=True) #p2c-21-085

    def __str__(self): #p2c-21-085
        return self.events_name #p2c-21-085


from django.db import models

# Create your models here.
