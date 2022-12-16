from flask import Flask
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    return 'admin'

@app.route('/', methods=["GET"])
@auth.login_required
def hello_world():
    return f"Oxigenai Gaba (user {auth.current_user()})"

if __name__ == '__main__':
    app.run()
