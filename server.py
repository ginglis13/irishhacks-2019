import sys
import json

from flask import Flask, render_template, make_response, request
from backend.account import Person, Organization 
from backend.post import Post

sys.path.append('./frontend')
sys.path.append('./backend')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help")
def help():
    return render_template("help.html")


# TODO needs authentication
@app.route("/edit/post/<postid>")
def edit_post(postid):
    post = Post.init_from_uid(postid)
    # TODO edit the post object
    # TODO save the post object
    return "edit post {}".format(postid)


# TODO needs authentication
@app.route("/edit/profile/<userid>")
def edit_profile(userid):
    person = Person.init_from_uid(userid)
    # TODO edit the person object
    # TODO save the person object
    return "edit profile {}".format(userid)


@app.route("/login")
def login():
    """
    email       (string)
    password    (string)
    """
    # we need to give the user a cookie, if they are not logged in, so that we can figure out if they are validated?
    return render_template("login.html")


@app.route("/signup")
def signup():
    """
    email    (string)
    password (string) **not hashed yet!
    """
    return "signpup"


# TODO if they are logged in, they can respond to the post
@app.route("/posts")
def posts():
    """
    we are going to have some filtering going on...
    """
    return "posts"


@app.route("/user_profile/<userid>")
def user_profile(userid):
    """
    userid (string)
    first_name (string)
    last_name (string)
    phone_number (number)
    email (string)
    """

    return userid


@app.route("/org_profile/<userid>")
def org_profile(userid):
    """
    userid (string)
    first_name (string)
    last_name (string)
    phone_number (number)
    email (string)
    """

    return userid


@app.route("/test", methods=["GET", "POST"])
def test():
    print(request.json)
    return json.dumps({"status": "success"})
    # name = request.cookies.get('userID')
    # if not name:
    #     resp = make_response(render_template('test.html'))
    #     resp.set_cookie('userID', "my_cookie")
    #     print(resp)
    #     print("NO COOKIES")
    #     return resp

    # return '<h1>welcome '+name+'</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='41001')
