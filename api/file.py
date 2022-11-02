from flask_restful import Resource, Api,reqparse
from flask_jwt_extended import get_jwt_identity,jwt_required
from werkzeug.datastructures import FileStorage
import datetime

from models import user
from service import user_service
from utils import response
from utils.code import StatusCode
from app import app



file_save_path = app.config["FILE_PATH"]
file_url_prefix = app.config["FILE_URL_PREFIX"]

class File(Resource):

    @jwt_required()
    def post(self):
        username = get_jwt_identity()

        code,user = user_service.find_user(username)

        args = reqparse.RequestParser() \
            .add_argument("file", type=FileStorage, location='files') \
            .parse_args()

        if user == None:
            return response(400,code.code,code.message)
        else:
            # print(user)
            file = args['file']
            print(file.filename)
            curtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
            print(curtime)
            file.filename = curtime+'.'+file.filename.split('.')[1]
            file_url = file_save_path+file.filename
            file.save(file_url)
            data = {
                "file_url": file_url_prefix+file.filename,
            }
            return response(200,code.code, code.message,data)

            


