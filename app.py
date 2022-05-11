from flask import Flask
from flask import request
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, OPI!</p>"


@app.route("/params")
def parameters():
    ## Test : http://127.0.0.1:5000/params?username=Miguel&email=m.escalante@opianalytics.com
    username = request.args.get('username')
    email = request.args.get('email')
    return f"{username}: {email}"


@app.route("/fakepost")
def fpost():
    data = request.data
    return data


@app.route("/truepost", methods=['POST'])
def tpost():
    data = request.data
    return data


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


if __name__ == "__main__":
    app.run(debug=True)
