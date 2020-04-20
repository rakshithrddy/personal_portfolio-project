from django.db import models
import datetime


class BlogProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(datetime.datetime.now())

    def __str__(self):
        return self.title