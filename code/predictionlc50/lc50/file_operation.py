import pickle
import os
from .logs import Logger



class File_operation:
    def __init__(self):
        self.log_fileobj=open("Logs/File_operation_Log.txt", 'a+')
        self.log_writer=Logger()




    def Delete_Existing_file(self,filename):
        """
                                  Method Name: Delete_Existing_file
                                  Description: This function is used to Delete Existing file  
                                  
                                  filename:name of filename to delete 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """


        self.filename=filename
        try:
            for i in os.listdir():
                if i==self.filename:
                    os.remove(self.filename)
                    self.log_writer.log(self.log_fileobj, '{} file deleted succssfully'.format(self.filename))
        except:
            self.log_writer.log(self.log_fileobj, 'Error in Deleting Existing file-{}'.format(self.filename))
        # self.filename=filename
        # if os.path.isdir(filename):
        #     os.remove(self.filename)


    def Save_Model(self,model):
        """
                                  Method Name: Save_Model
                                  Description: This function is used to save the model for future usecases
                                  model:model to saved
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.model=model
        filename='Rf_model.sav'
        
        self.Delete_Existing_file(filename)
        try:

            pickle.dump(self.model,open(filename,'wb'))
            self.log_writer.log(self.log_fileobj, 'model saved succssfully ')
        except:
            self.log_writer.log(self.log_fileobj, 'Error in saving model-{}'.format(filename))

    def Load_Model(self,filename):
        """
                                  Method Name: Insert_Into_Database
                                  Description: This function is used to Load the model form saved model file 
                                  filename:name of file in which model is saved
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.filename=filename
        try:

            model_file=pickle.load(open(self.filename,'rb'))
            

            return model_file

        except:
            self.log_writer.log(self.log_fileobj, 'Error in loading module')