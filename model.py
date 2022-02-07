from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":

        clf = joblib.load("clf.pkl")

        height = request.form.get("height")
        weight = request.form.get("weight")

        X = pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])

        prediction = clf.predict(X)[0]

    else:
        prediction = ""

    return render_template("index.html", output = prediction)

if __name__ == '__main__':
    app.run(debug = True)