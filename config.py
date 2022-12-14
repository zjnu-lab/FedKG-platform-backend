
from logging import root
import os

import sys
import datetime


# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


user = 'root'
password = '123456'
host = '127.0.0.1'
port = '3306'
database = 'fedkg'

GRAPH_URL= "bolt://localhost:7687"
GRAPH_PWD = 'password'



# dev_db = prefix + 'data.db'
dev_db ='mysql+pymysql://%s:%s@%s:%s/%s' % (user, password, host, port,database)
# SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

SECRET_KEY = 'some-secret-string'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=60)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(minutes=60)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

#file path

FILE_PATH = "/Users/lzh17/Projects/FedKG-platform-backend/tempfile/"
FILE_URL_PREFIX = "127.0.0.1:5000/static/"