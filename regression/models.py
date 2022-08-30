from unicodedata import name
from django.db import models

# Create your models here.
class esm(models.Model):

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class parameters(models.Model):

    coe = models.IntegerField()
    intercept = models.IntegerField()
    name = models.ForeignKey(esm , on_delete=models.CASCADE , related_name='esmesh')



class Regres(models.Model):

    x = models.PositiveIntegerField()
    y= models.PositiveIntegerField()
    param = models.ForeignKey(parameters , on_delete=models.CASCADE , related_name='params')
    name = models.ForeignKey(esm , on_delete=models.CASCADE , related_name='esme')

    

