from flask import Flask

from api import register_api



def create_app():
    app = Flask(__name__)
    register_api(app)

    return app


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

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)