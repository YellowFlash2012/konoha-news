from datetime import datetime
from enum import unique
from flask import Flask, render_template, url_for, flash
from sqlalchemy.orm import backref
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from posts import posts
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '31a1a8c2a033332e089e4432471d15ce'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"
# user_1 = User(username='Isshiki', email='issiki@kara.org', password='kawaki')
# db.session.add(user_1)
# user_2 = User(username='Amado', email='amado@kara.io', password='kashinkoji')
# db.session.add(user_2)
# db.create_all()
# db.session.commit()
#print(User.query.all())
#print(User.query.first())
#print(User.query.filter_by(username='Amado').all())
# user = User.query.get(1)

# post_1 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
# post_2 = Post(title='Blog 2', content='Second Post Content', user_id=user.id)
# db.session.add(post_1)
# db.session.add(post_2)
# db.session.commit()
# print(user.posts)
# db.drop_all()
db.create_all()

# *******************routes****************
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
