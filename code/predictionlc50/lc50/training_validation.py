from re import S
from .file_validation import File_Validation
from .train_model import Data_Validation
from .model_creation import Model_Create
from .file_operation import File_operation
from .data_moving import Data_Moving
from .DB_operations import Cassandra_Management 
from .logs import Logger
import re



class Train_Validation:
    def __init__(self,path,email,NumberofColumns,number_of_files,column_names):
        self.email=email
        self.NumberofColumns=NumberofColumns
        self.number_of_files=number_of_files
        self.column_names=column_names
        self.filename="total_data.csv"
        self.file_validate=File_Validation(path)
        self.data_validation=Data_Validation()
        self.model_create=Model_Create()
        self.file_operation=File_operation()
        self.cassandra_management=Cassandra_Management()
        self.data_moving=Data_Moving()
        self.log_fileobj=open("Logs/Training_validation_Log.txt", 'a+')
        self.log_writer=Logger()


#DSA-Data Sharing Agreement

    def train_validation(self):
        try:
            self.log_writer.log(self.log_fileobj, 'Start of Training Validation on files!!')

            try:

                self.log_writer.log(self.log_fileobj, 'Start of file validation')
                #file number checking which is in DSA
                self.file_validate.file_counter(self.number_of_files)
                self.log_writer.log(self.log_fileobj, 'File counter validation is completed')

                regex=self.file_validate.manual_regex_creation()#regex creation to check the filename
                self.log_writer.log(self.log_fileobj, 'Regex created')

                self.file_validate.file_name_check(regex)#file name check -
                #if file name is not in format then moved to bad_raw folder
                self.log_writer.log(self.log_fileobj, 'File name checked')

                self.file_validate.no_of_columns_check(self.NumberofColumns)
                #column names are not given 
                #column names are giving
                self.file_validate.give_colnames(self.column_names)

                self.log_writer.log(self.log_fileobj, 'Number of columns checked and column names are given ')
                #checking missing values in whole column
                self.file_validate.validateMissingValuesInWholeColumn()
                self.log_writer.log(self.log_fileobj, 'Checking of missing values in whole column is checked')
                self.log_writer.log(self.log_fileobj, 'Raw validation is completed...')
            except:
                self.log_writer.log(self.log_fileobj, 'Error in file validation')
            try:
                #sending a notification to client about data files
                
                self.file_validate.Notification_To_Client(self.email)
                self.log_writer.log(self.log_fileobj, ' sending of Notification to client about validation-good data/bad data-completed')
                
                self.file_validate.Concanating_Data(self.filename)
                #concating a data to handled easy
                self.log_writer.log(self.log_fileobj, 'Data are marged..in one file-{}'.format(self.filename))
            except:

                self.log_writer.log(self.log_fileobj, 'Error in notification and concanitaing data')
            #storing data in database

            try:

                #database operations
                self.log_writer.log(self.log_fileobj, 'Starting of database operation :casasandra')
                conn=self.cassandra_management.Create_Connection()#cassandra connection
                self.log_writer.log(self.log_fileobj, 'database connection is created')

                self.cassandra_management.Create_Table(conn)#table created in database
                self.log_writer.log(self.log_fileobj, 'table is created in database')

                self.cassandra_management.Insert_Into_Database(conn,self.filename)#data inserted in database
                
                self.log_writer.log(self.log_fileobj, 'Data insertion in database is completed')
            
            except:

                self.log_writer.log(self.log_fileobj,'Error in database operation')

            #data moved to archived folder
            try:

                self.log_writer.log(self.log_fileobj, 'Data moving into  archived folder is started')
                #Data moving in archived folder for future reference
                self.data_moving.Datamoving_Good_Raw()#good data moving

                self.data_moving.Datamoving_Bad_Raw()#Bad data moving

                self.log_writer.log(self.log_fileobj, 'data moving into archived folder is complated')

            except:

                self.log_writer.log(self.log_fileobj, 'Error in data moving archived folder')
            #data validation

            try:

                self.log_writer.log(self.log_fileobj, 'Data validation is started')
                data=self.data_validation.Create_Instance()#instance of data

                df=self.data_validation.Remove_Columns(data)#remove unwanted columns

                NullPreasent=self.data_validation.Check_Missing_Values(data)#checking missing values
                
                #pandas report 
                self.data_validation.Pandas_Report(df)


                self.data_validation.Check_Outliers(df)#outliers are checking

                self.log_writer.log(self.log_fileobj, 'Data validation is completed')

            except:
                self.log_writer.log(self.log_fileobj, 'Error in data validation')
            # df_new=self.data_validation.Handled_Outliers(df)

            try:
                self.log_writer.log(self.log_fileobj, 'data preprocessing is started')
                #seperate label and feature
                x,y=self.data_validation.Separate_Label_Feature(df)

                self.log_writer.log(self.log_fileobj, 'feature and label is seperated')
                #train and test splitting 
                x_train,x_test,y_train,y_test=self.data_validation.Train_Test_Split(x,y)

                self.log_writer.log(self.log_fileobj, 'Data validation is complated')

            except:

                self.log_writer.log(self.log_fileobj, 'Error in data preprocessing')

            try:


            #model create
                self.log_writer.log(self.log_fileobj, 'Model creation is started')
                model=self.model_create.Train_Model(x_train,y_train)#model creation

                self.log_writer.log(self.log_fileobj, 'Model training is completed')
                self.file_operation.Save_Model(model) 
                #model is saved for future reference
                self.log_writer.log(self.log_fileobj, 'model is saved-Rf_model.sav')
                #checking score of model
                score=self.model_create.Check_score(x_test,y_test,model)
                self.log_writer.log(self.log_fileobj, 'Score  of the model is -{}'.format(score))

            except:

                self.log_writer.log(self.log_fileobj, 'Error in model creation')
            self.log_writer.log(self.log_fileobj, 'validation is completed')
            self.log_writer.log(self.log_fileobj, 'Training part is completed')

            return model,score

        except:
            
            self.log_writer.log(self.log_fileobj, 'Error in Training part')

        
        


