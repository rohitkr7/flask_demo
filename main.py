from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "This is a demo flask homepage"


@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", name=username)


if __name__ == "__main__":
    app.run(debug=True)
