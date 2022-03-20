from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    fb_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name