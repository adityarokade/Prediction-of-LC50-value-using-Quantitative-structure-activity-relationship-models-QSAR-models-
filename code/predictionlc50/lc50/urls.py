from os import name
from django.urls import path


from .import views
urlpatterns = [
    path('',views.home),
    path('pre_train/',views.pre_training),
    path('train/',views.training_model,name="train"),
    path('prediction/',views.prediction),
    #path('result{Username:Username}/',views.result, name="result")
    path('result/<int:id>/',views.result),
    path('pandas_report/',views.Pandas_Report)
]