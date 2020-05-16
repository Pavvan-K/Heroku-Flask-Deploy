from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to deployed app!"



if __name__=="__main__":
    app.run(port=8000)