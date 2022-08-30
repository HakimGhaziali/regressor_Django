from django.db import models

# Create your models here.




class Regres(models.Model):

    x = models.PositiveIntegerField()
    y= models.PositiveIntegerField()



class parameters(models.Model):

    coe = models.IntegerField()
    intercept = models.IntegerField()
    regre = models.ForeignKey(Regres , on_delete=models.CASCADE , related_name='regression')

