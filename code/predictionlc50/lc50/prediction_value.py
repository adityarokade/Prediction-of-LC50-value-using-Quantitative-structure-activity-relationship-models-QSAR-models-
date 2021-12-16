from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from .logs import Logger




class Predict:
    def __init__(self):
        self.log_fileobj=open("Logs/prediction_value_Log.txt", 'a+')
        self.log_writer=Logger()


    def Prediction_Process(self,CIC0,SM1_Dz,GATS1i,NdsCH,NdssC,MLOGP):
        """
                                  Method Name: Prediction_Precess
                                  Description: This function is use to craete a 2D array for prediction purpose
                                  of prediction 
                                  input:It gets a input values create a 2D array -CIC0,SM1_Dz,GATS1i,NdsCH,NdssC,MLOGP
                                  Output: 2Darray
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
       
        self.CIC0=CIC0
        self.SM1_Dz=SM1_Dz
        self.GATS1i=GATS1i
        self.NdsCH=NdsCH
        self.NdssC=NdssC
        self.MLOGP=MLOGP
        try:

            values=[[self.CIC0,self.SM1_Dz,self.GATS1i,self.NdsCH,self.NdssC,self.MLOGP]]

            return values
        except:
             self.log_writer.log(self.log_fileobj, 'Error in creating 2D array of prediction data')
        

    def prediction(self,values,model):
        """
                                  Method Name: prediction
                                  Description: This function is used to calculate the concentration os LC50
                                  by using 6 different values
                                  values:2D array -6 different values
                                  model:model from which prediction is done                                  
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """

        self.value=values
        self.model=model
        try:
            predict_value=self.model.predict(self.value)
            self.log_writer.log(self.log_fileobj, 'prediction done succssfully...')
            return predict_value
        except:
             self.log_writer.log(self.log_fileobj, 'Error in doing  prediction')
    

    

    



