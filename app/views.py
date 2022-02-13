from flask import render_template
from .request import get_random_quote
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - diary of a whimpy junior developer'
    #making api call
    random_quote=get_random_quote()
    
    return render_template('index.html',title=title,random_quote=random_quote)


@app.route('/random_quote/<int:random_quote_id>')
def random_quote(random_quote_id):

    '''
    View random quote page function that returns the random_quote page and its data
    '''
    return render_template('random_quote.html',id = random_quote_id)