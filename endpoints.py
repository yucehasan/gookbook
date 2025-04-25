from flask import Blueprint, jsonify, render_template, request
from models import User, db

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('index.html', name="Yuce")

@router.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return render_template('add_user_success.html', name=name)
    return render_template('add_user.html')

@router.route('/users')
def view_users():
    users = User.query.all()
    return render_template('users.html', users=users)
