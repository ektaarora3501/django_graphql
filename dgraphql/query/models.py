from django.db import models

# Create your models here.

class Writer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Books(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ManyToManyField(Writer)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

        
