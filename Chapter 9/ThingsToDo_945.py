# 9.4 & 9.5
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    return render_template("home.html", thing=thing, height=height, color=color)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
