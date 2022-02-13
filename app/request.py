from app import app
import urllib.request,json
from .models import Random_Quote



# Getting the random quote base url
base_url = app.config["RANDOM_QUOTE_BASE_URL"]


#api call
def get_random_quote():
    '''
    Function that gets the json response to our url request
    '''
    

    with urllib.request.urlopen(base_url) as url:
        get_random_quote_data = url.read()
        get_random_quote_response = json.loads(get_random_quote_data)

        random_quote_results = None



    if get_random_quote_response:
       id=get_random_quote_response.get('id')
       quote=get_random_quote_response.get('quote')
       author=get_random_quote_response.get('author')
      
       random_quote_results=Random_Quote(id,quote,author)

       return random_quote_results

