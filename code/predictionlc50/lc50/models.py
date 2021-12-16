from django.db import models

# Create your models here.
class Prediction(models.Model):
    User_name=models.CharField(max_length=80)
    Lab_name=models.CharField(max_length=120)
    Email=models.EmailField(max_length=150)

    CIC0=models.FloatField(max_length=50)
    SM1_Dz=models.FloatField(max_length=50)
    GATS1i=models.FloatField(max_length=50)
    NdsCH=models.FloatField(max_length=50)
    NdssC=models.FloatField(max_length=50)
    MLOGP=models.FloatField(max_length=50)
    
    Concentration_LC50=models.FloatField(max_length= 50)