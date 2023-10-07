from . import auth
from flask import render_template, request,redirect, url_for, flash 
from ..forms import Login, SignUpForm
from ..social.api import pokemon_api
from ..models import db, User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up(): 
    form = SignUpForm()
    if current_user.is_authenticated:
        return redirect(url_for('social.index'))
    if request.method == 'POST':
        if form.validate(): 
            username = form.Username.data
            email= form.Email.data
            password= form.Password.data
        
            user = User(username,email,password)

            db.session.add(user)
            db.session.commit()

            flash('Successfully created your account. Sign in now.', "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid form. Please try again.", 'error')

    return render_template('sign-up.html', form=form)


@auth.route('/login', methods=['GET','POST'])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('social.index'))
    if request.method == 'POST':
        if form.validate():
            username = form.Username.data
            password = form.Password.data
            user = User.query.filter_by(username=username).first()

        if user: 
            if check_password_hash(user.password, password):
            # if passwords match, consider them logged in
                    login_user(user)
                    flash('Successfully logged in.')
                    return redirect(url_for('social.index'))
            else:
                flash('Incorrect username/password.', 'danger')
        else:
            flash('That username or password does not exist.', 'danger')
            return render_template('login.html', form = form)
    return render_template('login.html', form = form)



@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('social.index'))