from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<user>')  # for logged in user
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/shopping')
def shopping():
    food = ["cheese", "Tuna", "Beef", "toothpaste"]
    return render_template("shopping.html", food=food)


@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", name=username)


if __name__ == "__main__":
    app.run(debug=True)
