from django.shortcuts import redirect, render
from .forms import PredictionForm
from .models import Prediction
from .training_validation import Train_Validation
from .prediction_value import Predict
from .file_operation import File_operation
import time
# Create your views here
def home(request):
    
    return render(request,'home.html')

# Training part
def training_model(request):
    path="training_data/"
    email="abc@gmail.com"
    NumberofColumns=7
    number_of_files=1
    column_names=['CIC0','SM1_Dz(Z)','GATS1i','NdsCH','NdssC','MLOGP','LC50']
    train_obj=Train_Validation(path,email,NumberofColumns,number_of_files,column_names)
    model,score=train_obj.train_validation()

    # print("training part")
    # time.sleep(40)S
    # if model is not None:
    #     time.sleep(30)
    #     return redirect('/')
    

    return render(request,"train.html")

def pre_training(request):

    return render(request,"pre_train.html")

def prediction(request):
    try:

        if request.method == 'POST':
            fm = PredictionForm(request.POST)
            if fm.is_valid():
                User_name= fm.cleaned_data['User_name']
                Lab_name = fm.cleaned_data['Lab_name']
                Email= fm.cleaned_data['Email']
                CIC0 = fm.cleaned_data['CIC0']
                SM1_Dz = fm.cleaned_data['SM1_Dz']
                GATS1i = fm.cleaned_data['GATS1i']
                NdsCH = fm.cleaned_data['NdsCH']
                NdssC= fm.cleaned_data['NdssC']
                MLOGP = fm.cleaned_data['MLOGP']
                try:

                    predict_obj=Predict()
                    fileoperation_obj=File_operation()
                    values=predict_obj.Prediction_Process(CIC0,SM1_Dz,GATS1i,NdsCH,NdssC,MLOGP)
                    model_file='Rf_model.sav'
                    model=fileoperation_obj.Load_Model(model_file)
                    predict_value=predict_obj.prediction(values,model)
                #predict_value=3.5
                except:
                    print("error in getting prediction value")
                

                
                mo=Prediction(User_name=User_name,Lab_name=Lab_name,Email=Email,CIC0=CIC0,SM1_Dz=SM1_Dz,GATS1i=GATS1i,NdsCH=NdsCH,NdssC=NdssC,MLOGP=MLOGP,Concentration_LC50= predict_value)
                
                mo.save()
            
                id=mo.id
                return redirect('/result/{}/'.format(id))


                
        else:
                fm = PredictionForm()
    except:
        pass
    

    return render(request, 'prediction.html', {'form':fm})
    
    

def result(request,id):
    try:

        data=Prediction.objects.get(id=id)
    except:
       pass




    return render(request,"result.html",{'data':data})

def Pandas_Report(request):
    return render(request,"Pandas_Report.html")