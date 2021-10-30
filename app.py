from flask import Flask, render_template, url_for, flash
from werkzeug.utils import redirect
from posts import posts
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '31a1a8c2a033332e089e4432471d15ce'

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for('home'))
    return render_template("register.html", form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Welcome {form.username.data}", "success")
        return redirect(url_for('home'))
    return render_template("login.html", form=form, title='Login')

if __name__ == "__main__":
    app.run(debug=True)
