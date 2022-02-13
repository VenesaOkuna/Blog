from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_random_quote
from flask_login import login_required

# Views


@main.route('/' )
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    #making api call
    quote=get_random_quote()
    title = 'Home - diary of a whimpy junior developer'
    
    return render_template('index.html',title=title,quote=quote)


