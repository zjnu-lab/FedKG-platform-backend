from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS



app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy()
db.init_app(app)
jwt = JWTManager(app)


from api import register_api
register_api(app)

CORS(app, supports_credentials=True)



def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    register_api(app)
    

    return app,db


# api = Api(app)

# api.add_resource(Hello, '/')


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"



# def register_api(app):

#     api = Api(app)

#     #hello_world
#     api.add_resource(Hello, '/')

#     #user
#     api.add_resource(Users, '/users')
#     api.add_resource(User, '/user/<user_id>')


#     #auth
#     api.add_resource(Login, '/login')
#     api.add_resource(Register, '/register')

# if __name__ == '__main__':
#     # app,db = create_app()
#     app.run(debug=True)