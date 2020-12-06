from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField('date_posted', auto_now_add=True)

    def __str__(self):
        return self.title