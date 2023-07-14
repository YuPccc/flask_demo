
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, chain!'

@app.route('/book/list')
def get_book():
    page=request.args.get("page", default=1, type=int)
    return f'{page}'


if __name__ == '__main__':
    app.run( debug=True)
