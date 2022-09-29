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

    list = []

    for j in search(item, tld="com", num=10, stop=10, pause=2):
    	# print(j)
        list.append(j)

    return list


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
    
    res = requests.get(url,verify=False)

    soup = bs(res.content,'html.parser').text

    soup = soup.replace('\n','').replace('\t','')

    return soup


from google.cloud import language_v1

def sample_analyze_entities(text_content,URL,saliance_score):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.HTML

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

    list = []

    # Loop through entitites returned from the API
    for entity in response.entities:
        entity_name = entity.name

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        entity_type = language_v1.Entity.Type(entity.type_).name

        # Get the salience score associated with the entity in the [0, 1.0] range
        saliance = entity.salience

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.

        # metadata = []
        # for metadata_name, metadata_value in entity.metadata.items():
            # meta_name = metadata_name, 
            # meta_value = metadata_value
            # dict_meta = {'meta_name':meta_name, 'meta_value':meta_value} 
            # metadata.append(dict_meta)

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        mentions = []
        for mention in entity.mentions:
            mentions_text = mention.text.content

            if mentions_text not in mentions:

                mentions.append(mentions_text)

            # Get the mention type, e.g. PROPER for proper noun
            # mentions_type = language_v1.EntityMention.Type(mention.type_).name

            # dict_mentions = {'mentions_text':mentions_text}#, 'mentions_type':mentions_type}
            # mentions.append(dict_mentions)

        dict = {'URL':URL ,'entity_name':entity_name, 'entity_type':entity_type, 'saliance':saliance, 'mentions':mentions}

        if saliance >= saliance_score:

            list.append(dict)

    return list
