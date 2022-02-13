from flask import render_template
from .request import get_random_quote
from app import app

# Views


@app.route('/' )
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    #making api call
    quote=get_random_quote()
    title = 'Home - diary of a whimpy junior developer'
    return render_template('index.html',title=title,quote=quote)


