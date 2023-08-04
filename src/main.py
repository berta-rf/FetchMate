from flask import Flask, render_template
import os
import random


app = Flask(__name__)

images = os.listdir("src/static/img")
image = random.choice(images)


@app.route("/")
def home():
    return render_template("index.html", image=image)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/breed")
def breed():
    return render_template("breed.html")


@app.route("/results/")
def results():
    # mimics database results from quiz
    breeds = [
        "First breed",
        "Second breed",
        "Third breed",
        "Fourth breed",
        "Fifth breed",
    ]

    return render_template("results.html", breeds=breeds)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
