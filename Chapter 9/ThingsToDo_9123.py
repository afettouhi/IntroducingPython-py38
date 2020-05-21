# 9.1, 9.2 & 9.3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "It's alive!"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
