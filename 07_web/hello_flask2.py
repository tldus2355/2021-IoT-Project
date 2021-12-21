from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
        return render_template("hello.html", title="Hello, Flask!!")

@app.route("/first")
def first():
    return render_template("first.html", title="first")

@app.route("/second")
def second():
    return render_template("second.html", title="second")

# 터미널에서 직접 실행시켰다면
if __name__ == "__main__":
    app.run(host="0.0.0.0")