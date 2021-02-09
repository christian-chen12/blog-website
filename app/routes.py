from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

# index route/home page
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Cooper'}
    posts = [
        {
            'author': {'username': 'Amielya'},
            'body': 'Spiders'
        },
        {
            'author': {'username': 'Cooper'},
            'body': 'Traveling is fun'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

# uses flask-login to allow users to log in and their information be remebered
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



# uses flask-login to log out user and redirect them to the index page
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



