import os
from flask import Flask, g, render_template, flash, request , url_for, session
import urllib
import datetime
import gc


app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return wrap

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/ielts')
def ielts():
    return render_template("ielts.html")


@app.route('/toefl')
def toefl():
    return render_template("toefl.html")

@app.route('/usa')
def usa():
    return render_template("usa.html")

@app.route('/uk')
def uk():
    return render_template("uk.html")

@app.route('/australia')
def australia():
    return render_template("australia.html")

@app.route('/canada')
def canada():
    return render_template("canada.html")

@app.route('/newzealand')
def newzealand():
    return render_template("newzealand.html")

@app.route('/studyabroad')
def studyabroad():
    return render_template("studyabroad.html")


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    app.run(debug=True, use_reloader=True)
