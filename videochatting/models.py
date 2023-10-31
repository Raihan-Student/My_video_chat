from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField( max_length =252)
    phone = models.CharField( max_length = 12)
    feedback = models.TextField( )
    date = models.DateField()

    def __str__(self):
        return self.name