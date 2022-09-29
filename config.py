
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
port = '3366'
database = 'fedkg'



# dev_db = prefix + 'data.db'
dev_db ='mysql://%s:%s@%s:%s/%s' % (user, password, host, port,database)
# SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

SECRET_KEY = 'some-secret-string'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(minutes=1)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'