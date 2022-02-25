from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app) 
db.create_all()

@app.route('/users', methods=['GET'])
def show_all_users():
    users = User.query.all()
    return render_template('user_listing.html', users = users)


@app.route('/users', methods=['POST'])
def users_new():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()
    return redirect(f"users/{new_user.user_id}")



@app.route('/users/<int:user_id>/', methods=['GET'])
def show_user_page(user_id):

    user = User.query.get_or_404(user_id)
    return render_template('show_user.html', user = user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user_info(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    db.session.add(user)
    db.session.commit()
    return redirect('user_listing.html')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return render_template('delete.html')

@app.route('/users/<int:user_id>/create/new', methods=['POST'])
def posts_new_form(user_id):
    """Show a form to create a new post for a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template('create_post.html', user=user)

@app.route('/users/<int:user_id>/create/new', methods=['POST'])
def create_post(user_id):
    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['post_title'],
        content=request.content['post_content'],
        user = user)
    db.session.add(new_post)
    db.session.commit()
    return (f"/users/{user_id}")

# GET /users/[user-id]/posts/new
# Show form to add a post for that user.
# POST /users/[user-id]/posts/new
# Handle add form; add post and redirect to the user detail page.
# GET /posts/[post-id]
# Show a post.

# Show buttons to edit and delete the post.

# GET /posts/[post-id]/edit
# Show form to edit a post, and to cancel (back to user page).
# POST /posts/[post-id]/edit
# Handle editing of a post. Redirect back to the post view.
# POST /posts/[post-id]/delete
# Delete the post.