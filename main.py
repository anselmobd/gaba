from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return "Oxigenai Gaba"

if __name__ == '__main__':
    app.run()
