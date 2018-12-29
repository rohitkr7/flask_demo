from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "This is a demo flask homepage, Method used is %s" % request.method


@app.route('/tuna')
def tuna():
    return "<h2>Tuna is good!</h2>"


'''
@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hey There! " + username + "</h2>"
'''


@app.route('/profile/<username>')
def profile(username):
    return render_template("../profile.html", name=username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>Post id is: %s</h2>" % post_id


@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"


if __name__ == "__main__":
    app.run(debug=True)
