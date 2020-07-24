from datetime import datetime


from django.db import models


# Create your models here.
from user.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.email
