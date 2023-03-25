from django.db import models

# Create your models here.

#create a table called react
class React(models.Model):
    name = models.CharField(max_length=64)
    details = models.CharField(max_length=600)

    def __str__(self):
        return self.name
