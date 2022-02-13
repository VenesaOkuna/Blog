from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - diary of a whimpy junior developer'
    return render_template('index.html', title = title)


@app.route('/random_quotes/<int:random_quotes_id>')
def random_quotes(random_quotes_id):

    '''
    View random quote page function that returns the random_quotes page and its data
    '''
    return render_template('random_quotes.html',id = random_quotes_id)