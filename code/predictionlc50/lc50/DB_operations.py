from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
import csv
from .logs import Logger


class Cassandra_Management:
    def __init__(self):
        self.log_fileobj=open("Logs/DB_operation_Log.txt", 'a+')
        self.log_writer=Logger()



    def Create_Connection(self):
        """
                                  Method Name:Create_Connection
                                  Description: This function is used craete connection of cassandra of cloud platform 

                                  Output: connection to execute the query
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        try:
#creting connection to manage a database
            cloud_config= {
            'secure_connect_bundle': 'secure-connect-ml-lc50prediction.zip'}
            auth_provider = PlainTextAuthProvider('mKyYAIrEQjZfkOgEMrZWZYpI', 'gyB,E_2SEBntYUKtDeZJsDYjwU-.s8yDh8M1g2dlCaS+uPXZE9S0d_vZnrb-t9,Q,0Jda-1WU-ae6ZrvcH,LvyPy,s3Ep,H+6F7HZFeWQdplHO0IJfh0amm+-PsK4jWP')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            self.log_writer.log(self.log_fileobj, 'cassandra connection created succssfully..')
            return session
        except:
            self.log_writer.log(self.log_fileobj, 'Error in creating connection')
    def Create_Table(self,conn):
        """
                                  Method Name: Create_Table
                                  Description: This function is used create a column to store the data  
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.session=conn
        try:
            #table creation in xyz table
            

            self.session.execute("CREATE TABLE concentration_of_lc50.qsar_fish_toxicity(Unnamed  int PRIMARY KEY,CIC0 float, SM1_Dz float, GATS1i float,NdsCH float,NdssC float, MLOGP float, LC50 float );")
            self.log_writer.log(self.log_fileobj, 'Table created succssfully')

        except:
           self.log_writer.log(self.log_fileobj, 'Error in creating table')    
    def Insert_Into_Database(self,conn,filename):
        """
                                  Method Name: Insert_Into_Database
                                  Description: This function is used to Insert the data in database 
                                  in table format
                                  conn:connection of database
                                  filename:name of filename by which data is inserted 
                                  Output: None
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        self.session=conn
        self.filename=filename
        try:


            with open(self.filename,'r') as data:
                next(data)
                data_csv= csv.reader(data,delimiter=',')
                self.log_writer.log(self.log_fileobj, 'data reading to insert in table ')
        
                for i in data_csv:
                    #fetching a every line in list format to insert in database
                    self.session.execute("INSERT INTO concentration_of_lc50.qsar_fish_toxicity (Unnamed ,CIC0 , SM1_Dz , GATS1i ,NdsCH ,NdssC , MLOGP , LC50]) values(%s,%s,%s,%s,%s,%s,%s,%s)",[int(i[0]),float(i[2]),float(i[3]),float(i[4]),float(i[5]),float(i[6]),float(i[7]),float(i[8])])
                    self.log_writer.log(self.log_fileobj, 'data inserted succssfully..')


        except:
           self.log_writer.log(self.log_fileobj, 'Error in inserting data in table')



        #csv reader object
            # print(data_csv)
            # all_value= []
        # goodFilePath="./Training_Raw_files_validated/Good_Raw/"
        # onlyfiles = [f for f in os.listdir(goodFilePath)]
        
        # for file in onlyfiles:
        #     with open(goodFilePath+'/'+file, "r") as f:
        #             next(f)
        #             reader = csv.reader(f, delimiter="\n")
        #             for line in enumerate(reader):
        #                 for list_ in (line[1]):
        #                     self.session.execute('INSERT INTO xyz.qsar_fish_toxicity values ({values})'.format(values=(list_)))
        # pass

    # def read_from_database(self,conn):
    #     self.session=conn
    #     self.fileFromDb = 'Prediction_FileFromDB/'
    #     self.fileName = 'InputFile.csv'

    #     select = "SELECT *  FROM Good_Raw_Data"
    #     self.session.execute(select)