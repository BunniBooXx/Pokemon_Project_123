from . import social
from flask import render_template, request,redirect, url_for, Blueprint
from ..forms import SearchForm, Login, SignUpForm
from .api import pokemon_api
from ..models import User
from flask_login import login_user, logout_user, current_user, login_required


@social.route('/', methods=['GET','POST'])
def index(): 
    form = SearchForm()
    if request.method == 'POST':
        if form.validate():
            query = form.query.data

            pokemon = pokemon_api(query)
            if pokemon :
                return render_template('index.html', pokemon=pokemon, form= form)
    return render_template('index.html', form = form )