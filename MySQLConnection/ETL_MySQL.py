#ETL_MySQL.py - v1.0.0
#Initial Publish - 3/28/2018
#Purpose - Provide an ETL flow for our connection to the MySQL database.
#Standing on the shoulders of Giants, much of the work is based off of
#	what Martin Yung wrote on CodeBurst.  You da real MVP!
#   https://codeburst.io/using-python-script-for-data-etl-53138c567906
#
#Prerequisites: Must install the following Python modules
#|-- mysql-connector-python (Connect to MySQL)
#|   |- https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
#|-- pyodbc (Connect to MS SQL)
#|	 |- https://github.com/mkleehammer/pyodbc/wiki
#|-- Psycopg2 (Connect to PostgreSQL)
#|   |- https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

#Bring in the important stuff
import sys

#Declare your constants and pull in arguments
mysql_db_config_import = [
  {
    'user': 'your_user_1',
    'password': 'your_password_1',
    'host': 'db_connection_string_1',
    'database': 'db_1',
  }
]#The database that we are pulling from

mysql_db_config_export = [
  {
    'user': 'your_user_1',
    'password': 'your_password_1',
    'host': 'db_connection_string_1',
    'database': 'db_1',
  }
]#The database we are exporting to

######################################
#SQL Server Configurations
#sqlserver_db_config = [
#  {
#   'Trusted_Connection': 'yes',
#    'driver': '{SQL Server}',
#    'server': 'your_sql_server',
#    'database': 'db1'
#    'user': 'your_db_username',
#    'password': 'your_db_password',
#    'autocommit': True,
#  }
#]
#####################################

#Build your selection query and pull the data from the database


#Clean/Transform the data as necessary


#Upload the data into the database.
#ForEach item in the array, attempt to insert
#Search existing database for key, 
#	if not present INSERT.  
#	If present, UPDATE
