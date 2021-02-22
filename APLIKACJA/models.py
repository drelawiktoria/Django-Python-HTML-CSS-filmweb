from django.db import models

# Create your models here.
class Film(models.Model):

    title = models.CharField(max_length=128)
    youtube = models.CharField(max_length=128, blank=True)
    description = models.TextField(default='')
    release_date = models.DateField(null=False, blank=False)
    length_video = models.IntegerField(default=0)
    rating_video = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title