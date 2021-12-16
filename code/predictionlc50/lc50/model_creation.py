from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn.ensemble import RandomForestRegressor
from .file_operation import File_operation
from .logs import Logger


class Model_Create:
    def __init__(self):
        self.file_operation=File_operation()
        self.log_fileobj=open("Logs/model_creation_Log.txt", 'a+')
        self.log_writer=Logger()  

    def Train_Model(self,x_train,y_train):
        """
                                  Method Name: Train_Model
                                  Description: This function is used to Training model
                                  
                                  Output: model
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            Rf_model=RandomForestRegressor(max_features='sqrt',min_samples_split=4)
            Rf_model.fit(x_train,y_train)
            self.log_writer.log(self.log_fileobj, 'model training is succssuful')
            return Rf_model
        except:
            self.log_writer.log(self.log_fileobj, 'Error in training model')
        
    


    def Check_score(self,x_test,y_test,dt_model):
        """
                                  Method Name: Check_score
                                  Description: This function is used to check the score of model
                                  
                                  Output: score
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:

            score=dt_model.score(x_test,y_test)
            self.log_writer.log(self.log_fileobj, 'Score of model is {}'.format(score))
            return score
        except:
            self.log_writer.log(self.log_fileobj, 'Error in checking score of model')
        

    