from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to FetchMate!"


@app.route("/breed-info")
def about():
    return "This is the info of the dog breed you searched"


@app.route("/quiz-result")
def contact():
    return "Your top 3 dog breeds!"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
