#ETL_SOAP.py - v1.0.0
#Initial Publish - 4/3/2018
#Purpose - Provide an ETL flow for our connection to the SOAP service.
#Standing on the shoulders of Giants, much of the work is based off of
#	what Martin Yung wrote on CodeBurst.  You da real MVP!
#   https://codeburst.io/using-python-script-for-data-etl-53138c567906
#

#Bring in the important stuff
import sys

#Declare your constants and pull in arguments
soapEndpoint = 'https://www.example.com/myServices/WSDL' #The WSDL

mysql_db_config_export = [
  {
    'user': 'your_user_1',
    'password': 'your_password_1',
    'host': 'db_connection_string_1',
    'database': 'db_1',
  }
]#The database we are exporting to


#Build your selection query and pull the data from the database


#Clean/Transform the data as necessary


#Upload the data into the database.
#ForEach item in the array, attempt to insert
#Search existing database for key, 
#	if not present INSERT.  
#	If present, UPDATE
