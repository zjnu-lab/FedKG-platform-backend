from flask import Flask
from flask_restful import Resource, Api

from api.Hello import Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/')

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)