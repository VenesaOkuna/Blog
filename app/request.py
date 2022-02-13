from xml.sax.saxutils import quoteattr
from app import app
import urllib.request,json
from .models import random_quote,quote

Random_Quote = random_quote.Random

# Getting the random quote base url
base_url = app.config["RANDOM_QUOTE_BASE_URL"]

def get_random_quote(category):
    '''
    Function that gets the json response to our url request
    '''
    get_random_quote_url = base_url.format(category)

    with urllib.request.urlopen(get_random_quote_url) as url:
        get_random_quote_data = url.read()
        get_random_quote_response = json.loads(get_random_quote_data)

        random_quote_results = None



    if get_random_quote_response:
       id=get_random_quote_response.get('id')
       author=get_random_quote_response.get('quote')
       content=get_random_quote_response.get('author')
       random_quote_results=Random_Quote(id,quote,author)

       return random_quote_results