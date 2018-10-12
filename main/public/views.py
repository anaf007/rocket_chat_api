# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from main.extensions import login_manager,rocket
from main.public.forms import LoginForm
from main.user.forms import RegisterForm
from main.user.models import User
from main.utils import flash_errors,templated

from pprint import pprint

from requests import put, get 



blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
@templated()
def home():
    """Home page."""

    url = 'http://localhost:5000/api/v1/auth/login'

    result = put(url, data={'username': 'anngle02','pwd':'anngle02'})

    userId = result.json()['userId']
    authToken = result.json()['authToken']

    # try:
    #     r = rocket.users_create(
    #         email='anngle02@163.com',
    #         name='anngle02',
    #         password='anngle02',
    #         username='anngle02'
    #     )
    # except Exception as e:
    #     print(ste(e))
    #     r = 'error'

    # print(r.json())

    # pprint(r)




    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return dict(form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
@templated()
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return dict(form=form)


@blueprint.route('/about/')
@templated()
def about():
    """About page."""
    form = LoginForm(request.form)
    return dict(form=form)
