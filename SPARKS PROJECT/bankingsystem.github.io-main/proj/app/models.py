from django.db import models
from django.utils.timezone import now

# Create your models here.
class Account(models.Model):
    cust_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="")
    balance = models.IntegerField()

    def __str__(self):
        return f"Account {self.id}"