from datetime import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod #to tell python not to expect self in this function
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
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
# db.create_all()
