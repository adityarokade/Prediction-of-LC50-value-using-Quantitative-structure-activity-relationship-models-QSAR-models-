from django.conf import settings
from django.core.mail import send_mail



class Notification:
    def __init__(self):
        pass



    def Email_notification(self,subject,message,email):
        """
                                  Method Name: Train_Model
                                  Description: This function is used to send a notification through email
                                  it sends a notification of how much data are useful or not
                                  
                                  Output: model
                                  On Failure: Exception

                                   Written By: Aditya Rokade
                                  Version: 1.0
                                  Revisions: None

                              """
        

        self.subject=subject
        self.message=message
        self.email=email
        # subject="Recivied Bad Files"
        # message="The file which you sended,is not in that format which is mention in aggrement.so to do project/to train maodel we need the file which is in correct format"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email]
        send_mail(self.subject,self.message , email_from ,recipient_list )
   
