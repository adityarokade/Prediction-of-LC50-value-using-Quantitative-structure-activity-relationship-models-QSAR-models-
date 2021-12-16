import os
import glob
import re
import shutil
import pandas as pd
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .file_operation import File_operation
from .email_notification import Notification
from .logs import Logger




class File_Validation:
    def __init__(self,path):
        self.path=path
        self.file_operation=File_operation()
        self.notification=Notification()
        self.log_fileobj=open("Logs/File_Validation_Log.txt", 'a+')
        self.log_writer=Logger()
    
    def DeleteExistingBaddataTrainingFolder(self):
        """
                                  Method Name: DeleteExistingBaddataTrainingFolder
                                  Description: This function delete existing bad_raw data folder if present . 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """

        path = 'Training_Raw_files_validated/'
        try:
            #this is used to delete existing folder -Bad_Raw if present by using os

            if os.path.isdir(path + 'Bad_Raw/'):#check the file is present or not
                shutil.rmtree(path + 'Bad_Raw/')#remove the file
                self.log_writer.log(self.log_fileobj, 'Existing Bad data folder Deleted')

        except:
            self.log_writer.log(self.log_fileobj, 'Error in Deleteing Existing Bad data folder')

    def DeleteExistingGooddataTrainingFolder(self):
        """
                                  Method Name: DeleteExistingGooddataTrainingFolder
                                  Description: This function delete existing good_raw data folder if present . 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        path = 'Training_Raw_files_validated/'
        try:
            #this is used to delete existing folder -Good_Raw if present by using os

            if os.path.isdir(path + 'Good_Raw/'):#check the file is present or not
                shutil.rmtree(path + 'Good_Raw/')#remove the file
                self.log_writer.log(self.log_fileobj, 'Existing Good data folder Deleted')
        except:
            self.log_writer.log(self.log_fileobj, 'Error in Deleteing Existing Good data folder')

    def createdirectoryforgoodandbadfile(self):
        """
                                  Method Name: createdirectoryforgoodandbadfile
                                  Description: This function create good and bad raw data folder to store raw data. 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """

        #calling a function to delete a pre existing folder of Good_Raw data and Bad_Raw data
        self.DeleteExistingBaddataTrainingFolder()
        self.DeleteExistingGooddataTrainingFolder()
        try:
            #creating a new folder of Good_Data and Bad_Data

            path1 = os.path.join("Training_Raw_files_validated/", "Good_Raw")
            if not os.path.isdir(path1):
                os.makedirs(path1)
                self.log_writer.log(self.log_fileobj, 'Good data folder created')
                
            path2 = os.path.join("Training_Raw_files_validated/", "Bad_Raw")
            if not os.path.isdir(path2):
                os.makedirs(path2)
                self.log_writer.log(self.log_fileobj, 'Bad data folder created')
        except:
            self.log_writer.log(self.log_fileobj, 'Error in creating Good and Bad data folder')


    
    def file_counter(self,number_of_files):
        """
                                  Method Name: file_counter
                                  Description: This function counts the total files in training folder .
                                  The count of files are getted by client .
                                  number_of_files:number of files in training folder
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """

        self.number_of_files=number_of_files
        self.createdirectoryforgoodandbadfile()
        try:
            #by using if-else condition checking a file number

            files=[f for f in os.listdir(self.path)]
            
            if len(files)==self.number_of_files:
                for filename in files:

                    shutil.copy(self.path +filename, "Training_Raw_files_validated/Good_Raw")
                    #if file number is matched then copied to Training_Raw_files_validated/Good_Raw
                    self.log_writer.log(self.log_fileobj, 'files are counted and it is correct')
                    self.log_writer.log(self.log_fileobj, 'files are copied to ../Training_Raw_files_validated/Good_Raw ')
            else:
                for filename in files:
                    shutil.copy(self.path + filename, "Training_Raw_files_validated/Bad_Raw")
                    #if file number is not matched then copied to Training_Raw_files_validated/Bad_Raw
                    self.log_writer.log(self.log_fileobj, 'files are counted and it is incorrect')
                    self.log_writer.log(self.log_fileobj, 'files are copied to Training_Raw_files_validated/Bad_Raw ')
        except:
            self.log_writer.log(self.log_fileobj, 'Error in File counter')




    def manual_regex_creation(self):
        """
                                  Method Name: manual regex creation
                                  Description: This function create a regex to validate file name 
                                  Output: regex pattern
                                  On Failure: Exception

                                  Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
      

        regex = "['qsar']+['_']+['fish']+['_']+['toxicity']+.csv"

        self.log_writer.log(self.log_fileobj, 'Regex created')
        return regex

    def file_name_check(self,regex):
        """
                                  Method Name: file name check
                                  Description: This function checks the file name based on 
                                  regex pattern ,if matched then ok.or mot matched then moved to Bad_Raw folder
                                  regex:regex pattern to check the filename
                                  Output: None
                                  On Failure: Exception

                                  Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            for filename in os.listdir("Training_Raw_files_validated/Good_Raw/"):
                if (re.match(regex, filename)):#file name checking by using regex pattern in re module
                    self.log_writer.log(self.log_fileobj, 'File are checked and which are matched   are as it is')

                else:
                    shutil.move("Training_Raw_files_validated/Good_Raw/" + filename, "Training_Raw_files_validated/Bad_Raw")
                    self.log_writer.log(self.log_fileobj, 'File are checked are which are not matched ,are moved to bad data folder')

        except:
            self.log_writer.log(self.log_fileobj, 'Error in File Name checking')


    def no_of_columns_check(self,NumberofColumns):
        """
                                  Method Name: no_of_columns_check
                                  Description: This function checks the number of columns in file ,
                                  if number of files are not matched then moved to Bad_Raw data folder. 
                                  Numberofcolumns:number of columns are provided by client in DSA.
                                  Output: None
                                  On Failure: Exception

                                  Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.NumberofColumns=NumberofColumns
        try:

            for file in os.listdir('Training_Raw_files_validated/Good_Raw/'):
                
                
                csv = pd.read_csv("Training_Raw_files_validated/Good_Raw/" + file,sep=";")
                if csv.shape[1] == self.NumberofColumns:
                    self.log_writer.log(self.log_fileobj, 'column numbers are checked and which are matched are as it is')

                else:
                    shutil.move("Training_Raw_files_validated/Good_Raw/" + file, "Training_Raw_files_validated/Bad_Raw")
                    self.log_writer.log(self.log_fileobj, 'column numbers are checked are which are not matched ,are moved to bad data folder')
        except:
            self.log_writer.log(self.log_fileobj, 'Error in Checking a column numbers')

    def give_colnames(self,column_names):
        """
                                  Method Name:give_colnames
                                  Description: This function gives column names  to data
                                  and then again saving the data in file.
                                  column_names:columns names provided by client
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.names=column_names
        for file in os.listdir('Training_Raw_files_validated/Good_Raw/'):
            try:

                csv = pd.read_csv("Training_Raw_files_validated/Good_Raw/" + file,sep=";",names=self.names)
                csv.to_csv("Training_Raw_files_validated/Good_Raw/" + file)
                self.log_writer.log(self.log_fileobj, 'column names are given succesfully')
            except:
                self.log_writer.log(self.log_fileobj,'Error in giving column names')

# names=['CIC0','SM1_Dz(Z)','GATS1i','NdsCH','NdssC','MLOGP','LC50']

    def validateMissingValuesInWholeColumn(self):
        """
                                  Method Name: validateMissingValuesInWholeColumn
                                  Description: This function checks the missing value in whole column
                                  if in any file found the missing value in whole column then file is moved 
                                  to Bad_Raw data folder. 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            for file in os.listdir('Training_Raw_files_validated/Good_Raw/'):
                csv = pd.read_csv("Training_Raw_files_validated/Good_Raw/" + file)
                
                for columns in csv:
                    if (len(csv[columns]) - csv[columns].count()) == len(csv[columns]):
                        
                        shutil.move("Training_Raw_files_validated/Good_Raw/" + file,"Training_Raw_files_validated/Bad_Raw")
                        
                        self.log_writer.log(self.log_fileobj,'{}-in this file we found the Missing value in whole column '.format(file))
                        self.log_writer.log(self.log_fileobj,'{} moved to bad data folder'.format(file))
                                        
                        break
                
                    else:
                        pass
        except:
            self.log_writer.log(self.log_fileobj, 'Error in validate Missing Values In Whole Column')


    def Notification_To_Client(self,email):
        """
                                  Method Name: Notification_To_Client
                                  Description: This is sub function which is used to send the mail nitification
                                  in notification we send the filenames which is bad and which is good to train a model
                                  email:Email of client to send notification 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.email=email
        try:
            goodfiles=[]
            badfiles=[]
            subject="About File Validation"
            for file in os.listdir('Training_Raw_files_validated/Good_Raw/'):
                goodfiles.append(file)
            for file in os.listdir('Training_Raw_files_validated/Bad_Raw'):
                badfiles.append(file)

            message="hellow sir, file validation is completed these files are good files {} and these files are Badfiles {}".format(goodfiles,badfiles)
            self.notification.Email_notification(subject,message,self.email)
            self.log_writer.log(self.log_fileobj, 'Notification sended to client')
                 
            

        except:
            self.log_writer.log(self.log_fileobj, 'Error in sending notification to client')



    def Concanating_Data(self,filename):
        """
                                  Method Name: Cocanating_Data
                                  Description: This function is used to concanate the data in one single file

                                  filename:filename in which data are concanated
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """


        self.filename=filename
        # filename="total_data.csv"
        try:

            for file in os.listdir('Training_Raw_files_validated/Good_Raw/'):
                csv = pd.read_csv("Training_Raw_files_validated/Good_Raw/" + file)
                self.file_operation.Delete_Existing_file(self.filename)
                csv.to_csv(self.filename,sep=",")
                self.log_writer.log(self.log_fileobj, 'data concaneted in {}'.format(self.filename))
        except:
            self.log_writer.log(self.log_fileobj, 'Error in concating data in one file')   










        # if os.listdir('../Training_Raw_files_validated/Good_Raw/')==1:
        #     for file in os.listdir('../Training_Raw_files_validated/Good_Raw/'):
        #         csv = pd.read_csv("./Training_Raw_files_validated/Good_Raw/" + file)

        #         csv.to_csv("total_data.csv",sep=",")
        # else:

        #     csvfile=[]
        #     for file in os.listdir('../Training_Raw_files_validated/Good_Raw/'):
        #         #csv = pd.read_csv("./Training_Raw_files_validated/Good_Raw/" + file)
        #         myfiles=glob.glob('AReM/{}/*.csv'.format(file))
        #         for j in myfiles:
        #             csvfile.append(j)


        #     df=pd.concat(map(pd.read_csv,csvfile),ignore_index=True)
        #     df.to_csv("totaldata.csv",sep=",")
            

    #         folder=os.listdir("AReM/")
    # csvfile=[]
    # for i in folder:
    #     myfiles=glob.glob('AReM/{}/*.csv'.format(file))
    #     for j in myfiles:
    #         csvfile.append(j)
        

    

    # df=pd.concat(map(pd.read_csv,csvfile),ignore_index=True)
    # df.to_csv("totaldata.csv",sep=",")



            
            