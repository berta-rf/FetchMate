from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import random


basedir = os.path.abspath(os.path.dirname(__file__))

# Create flask app
app = Flask(__name__)

# Setup database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Question class (questions table)
class Question(db.Model):

    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)

    question_text = db.Column(db.String(), nullable=False)

    param = db.Column(db.String(), nullable=False)

    answer_1 = db.Column(db.String(), nullable=False)
    answer_2 = db.Column(db.String(), nullable=False)
    answer_3 = db.Column(db.String(), nullable=False)
    answer_4 = db.Column(db.String(), nullable=False)
    answer_5 = db.Column(db.String(), nullable=False)

    value_1 = db.Column(db.Integer, default=1)
    value_2 = db.Column(db.Integer, default=2)
    value_3 = db.Column(db.Integer, default=3)
    value_4 = db.Column(db.Integer, default=4)
    value_5 = db.Column(db.Integer, default=5)

    def __repr__(self):
        return f"<Question {self.question_text}>"


######################################################################

# Dog background images to randomize for homepage
images = os.listdir("static/img")
image = random.choice(images)

# Home
@app.route("/")
def home():
    return render_template("index.html", image=image)


# About
@app.route("/about/")
def about():
    return render_template("about.html")


# Quiz
@app.route("/quiz")
def quiz():
    questions = enumerate(Question.query.all())
    return render_template("quiz.html", questions=questions)


# Quiz results
@app.route("/results")
def results():
    quiz_results = request.args
    # TODO: import matched_breeds method and output results
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
