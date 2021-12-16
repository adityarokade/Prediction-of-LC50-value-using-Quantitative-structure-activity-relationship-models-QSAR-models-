from django.core import validators
from django import forms
from .models import Prediction

class PredictionForm(forms.ModelForm):
    class Meta:
        model=Prediction
        fields=['User_name','Lab_name','Email','CIC0','SM1_Dz','GATS1i','NdsCH','NdssC','MLOGP']
        labels={'SM1_Dz':'SM1_Dz(Z)'}
        error_messages = {
        'User_name':{'required':'Name  is required'},
        'Lab_name':{'required':'Lab_name is required'},
        'Email':{'required':'Email is required'},
        'CIC0':{'required':'CIC0 is required'},
        'SM1_Dz':{'required':'SM1_Dz is required'},
        'GATS1i':{'required':'GATS1i is required'},
        'NdsCH':{'required':'NdsCH is required'},
        'NdssC':{'required':'NdssC is required'},
        'MLOGP':{'required':'MLOGP is required'}
         }