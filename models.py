"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


default_img = 'https://picsum.photos/200/300.jpg'


class User(db.Model):
    """User."""
    # def __repr__(self):
    #     p = self


    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    image_url = db.Column(db.String(500),
                    unique=True, default = default_img)
    
    # post = db.relationship('Post')
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Post(db.Model):
    """Post"""
    # def __repr__(self):
    #     p = self


    __tablename__ = "posts"

    post_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    content = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    created_at = db.Column(db.String(100),
                    nullable=False, unique=True)
    user_id = db.column(
                db.Text, 
                db.ForeignKey('users.user_id'))
                    