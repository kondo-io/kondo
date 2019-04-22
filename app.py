from flask import Flask, request
from flask_restplus import Resource, Api


app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.data  # data is empty
        # need posted data here


if __name__ == '__main__':
    app.run(debug=True)