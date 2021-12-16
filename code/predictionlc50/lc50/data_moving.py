import os
import shutil
from .logs import Logger


class Data_Moving:
    def __init__(self):
        self.Archived_folder_path="Archived_Data"
        self.Good_folder_path="Training_Raw_files_validated/Good_Raw/"
        self.Bad_folder_path="Training_Raw_files_validated/Bad_Raw/"
        self.log_fileobj=open("Logs/data_moving_Log.txt", 'a+')
        self.log_writer=Logger()

    def Datamoving_Good_Raw(self):
        """
                                  Method Name: Datamoving_Good_Raw
                                  Description: This function is used to moved the data in archived folder after creating one file
                                  so for future reference store the data in one folder  
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:
            onlyfiles=[f for f in os.listdir(self.Good_folder_path)]
            for file in onlyfiles:
                shutil.move(self.Good_folder_path +file, self.Archived_folder_path)
                self.log_writer.log(self.log_fileobj, 'Good data are moved to archived folder')
                
        except:
            self.log_writer.log(self.log_fileobj, 'Error in moving good data to archived folder')
    def Datamoving_Bad_Raw(self):
        """
                                  Method Name: Datamoving_Bad_Raw
                                  Description: This function is used to moved the data in archived folder 
                                  so for future reference store the data in one folder  
                                  Output: None
                                  On Failure: Exception

                                  Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:
            onlyfiles=[f for f in os.listdir(self.Bad_folder_path)]
            for file in onlyfiles:
                shutil.move(self.Bad_folder_path +file, self.Archived_folder_path)
                self.log_writer.log(self.log_fileobj, 'Bad data are moved to archived folder')

        except:
            self.log_writer.log(self.log_fileobj, 'Error in moving Bad data to archived folder')