import pandas as pd
import os
from pandas.core.frame import DataFrame
import seaborn as sns

from pandas_profiling import ProfileReport  
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from .file_operation import File_operation
from .logs import Logger

class Data_Validation:
    def __init__(self):
        self.file_operation=File_operation()
        self.log_fileobj=open("Logs/train_model_Log.txt", 'a+')
        self.log_writer=Logger()

    def Create_Instance(self):
        """
                                  Method Name: Create_Instance
                                  Description: This function is used to create a instance of data to do the data preprocessing
                                  
                                  Output: instance
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            csv=pd.read_csv("total_data.csv")
            self.log_writer.log(self.log_fileobj, 'Instance created succssfully')
            return csv
        except:
            self.log_writer.log(self.log_fileobj, 'Error in creating instance for data')

        
    def Remove_Columns(self,data):
        """
                                  Method Name: Remove_Columns
                                  Description: This function is used to remove the unwanted columns
                                  data:instanse of data
                                  Output: updated data 
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        
        try:

            data1=data.drop(["Unnamed: 0","Unnamed: 0.1"],axis=1)
            self.log_writer.log(self.log_fileobj, 'unwanted columns are removed succssfully...')
            return data1
        except:
            self.log_writer.log(self.log_fileobj, 'Error in removing unwanted columns')

                
        



    def Check_Missing_Values(self,data):
        """
                                  Method Name: Check_Missing_Values
                                  Description: This function is used to check the missing the values
                                  data:instanse of data
                                  Output: nullpresent
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.data=data
        self.nullpresent=False
        a=self.data.isnull().sum()
        try:

            for i in a:
                if i>0:
                    self.nullpresent=True
                    break
        except:
            pass
        return self.nullpresent
  


    def Pandas_Report(self,data):
        """
                                  Method Name: Pandas_Report
                                  Description: This function is used to get Pandas report
                                  data:instanse of data
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        filename="lc50/templates/Pandas_Report.html"
        
        self.data=data

        try:

            report=ProfileReport(self.data)
            #report.to_widgets()
            #self.log_writer.log(self.log_fileobj, 'bb1')
            self.file_operation.Delete_Existing_file(filename)
           # self.log_writer.log(self.log_fileobj, 'aa1')
            report.to_file(filename)
            #self.log_writer.log(self.log_fileobj, 'cc1')
        except:
            self.log_writer.log(self.log_fileobj, 'Error in creating pandas report...')
        

    

    def Check_Outliers(self,data):
        """
                                  Method Name: Check_Outliers
                                  Description: This function is used to check the outliers by using boxenplot
                                  data:instanse of data
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.df=data
        try:

            fig,ax=plt.subplots(figsize=(20,20))
            sns.boxenplot(data=self.df,ax=ax)
        except:
            pass
    

    def Handled_Outliers(self,data):
        try:

        
            q=data['CIC0'].quantile(.98)
            df_new=data[data['CIC0']<q]

            q=data['SM1_Dz(Z)'].quantile(.99)
            df_new=df_new[df_new['SM1_Dz(Z)']<q]

            q=data['GATS1i'].quantile(.99)
            df_new=df_new[df_new['GATS1i']<q]

            q=data['NdsCH'].quantile(.99)
            df_new=df_new[df_new['NdsCH']<q]

            q=data['NdssC'].quantile(.99)
            df_new=df_new[df_new['NdssC']<q]

            q=data['MLOGP'].quantile(.90)
            df_new=df_new[df_new['MLOGP']<q]

            q=data['LC50'].quantile(.95)
            df_new=df_new[df_new['LC50']<q]
        except:
            pass
        return df_new


    
    def Separate_Label_Feature(self,data):
        """
                                  Method Name: Separate_Label_Feature
                                  Description: This function is used to seperate Label and Feature columns
                                  data:instanse of data
                                  Output: feature,label
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            x=data.drop("LC50",axis=1)
            y=data.LC50

            return x,y
        except:
            self.log_writer.log(self.log_fileobj, 'Error in seperating label and feature columns ')
        

    
    def Train_Test_Split(self,x,y):
        """
                                  Method Name: Train_Test_Split
                                  Description: This function is used to spliting the data for testing and training part
                                  data:instanse of data
                                  Output: x_train,x_test,y_train,y_test
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=30,test_size=.20) 
            self.log_writer.log(self.log_fileobj, 'splitting is succssuful')  

        except:
            self.log_writer.log(self.log_fileobj, 'Error in splitting data')

        return x_train,x_test,y_train,y_test