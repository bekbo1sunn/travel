from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    
    
