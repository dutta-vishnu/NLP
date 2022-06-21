import requests
import json


from googlesearch import search
from bs4 import BeautifulSoup as bs


import requests
from bs4 import BeautifulSoup as bs

# !pip3 install --upgrade google-cloud-language
from google.cloud import language_v1
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../NLP/env/creds/hapreet_sir_medigence-928822fe8747.json'



def google_search(item):

    # to search
    # query = "Geeksforgeeks"

    search = []

    for j in search(item, tld="co.in", num=10, stop=10, pause=2):
    	# print(j)
        search.append(j)

    return search


def analyse_entity(text):
  
    client = language_v1.LanguageServiceClient()

    document = language_v1.types.Document(content=text, type=language_v1.types.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    import json

    result_json = response.__class__.to_json(response)

    result_dict = json.loads(result_json)

    return result_dict 


def classify_content(text):

    client = language_v1.LanguageServiceClient()

    document = language_v1.types.Document(content=text, type=language_v1.types.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document= document)

    response_json = response.__class__.to_json(response)

    import json

    response_dict = json.loads(response_json)

    return response_dict

def get_text_from_url(URL):
    
    url = URL
    
    res = requests.get(url)

    soup = bs(res.content).text

    return soup