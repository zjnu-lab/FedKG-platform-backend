from flask_restful import Resource, Api, reqparse


class Hello(Resource):
    def get(self):
        return 'hello_world',200

    def post(self):

        args = reqparse.RequestParser() \
            .add_argument('info', type = dict, required = True) \
            .parse_args()

        print(args)

        return 'test_post_json',200


