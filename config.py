
import os
import sys
import datetime


# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


# dev_db = prefix + 'data.db'
dev_db = prefix + os.path.join(os.getcwd(), 'data.db')
# SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

SECRET_KEY = 'some-secret-string'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(minutes=1)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'