from pprint import pprint

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


users = {
    "admin": generate_password_hash("234234",'pbkdf2:sha512:8000', 64),
}


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/', methods=["GET"])
@auth.login_required
def hello_world():
    return f"Oxigenai Gaba (user {auth.current_user()})"


if __name__ == '__main__':
    app.run()
