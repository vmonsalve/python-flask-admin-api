from peewee import *
from dotenv import load_dotenv
import os
import pymysql

load_dotenv() 

dba_name = os.getenv('DBA_NAME')
dba_user = os.getenv('DBA_USER')
dba_password = os.getenv('DBA_PASSWORD')
dba_host = os.getenv('DBA_HOST')
dba_port = os.getenv('DBA_PORT')


db = MySQLDatabase(dba_name, user=dba_user, password=dba_password, host=dba_host, port=int(dba_port))

class BaseModel(Model):
    class Meta:
        database = db