from peewee import *
from dotenv import load_dotenv
import os
import pymysql

load_dotenv() 

db = MySQLDatabase('access_system_api', user='root', password='vmonsalve', host='127.0.0.1', port=3306)

class BaseModel(Model):
    class Meta:
        database = db