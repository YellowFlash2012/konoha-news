from flask import render_template, url_for, flash, request, abort

from flaskblog.models import Post

from flask import Blueprint

main = Blueprint('main', __name__)


# *******************routes****************
@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("index.html", posts=posts)


@main.route('/about')
def about():
    return render_template("about.html")
