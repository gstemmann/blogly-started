from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
app.config['SECRET KEY'] = 'secret'
debug = DebugToolbarExtension(app)
db.create_all()

@app.route('/users', methods=['GET'])
def show_all_users():
    list = [1,2,3,4,4,5,6,7,7,7,7,7,774532,231,1,2]
    blue = [x for x in list if x > 4]
    users = User.query.all()
    return render_template('user_listing.html', blue = blue, users = users)

@app.route('/users/new', methods=['GET'])
def show_login_form():
    return render_template('create_account.html')

@app.route('/users/new', methods=['POST'])
def users_new():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/show', methods=['GET'])
def show_edit_user_page():
    return render_template('show_user.html')

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def show_edit_user_page():
    return redirect('user_listing.html')

@app.route('/users/<int:user_id>/delete', methods=['GET'])
def delete_user():
    return render_template ('user_listing.html')
