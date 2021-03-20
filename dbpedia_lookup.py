import requests
import json

URL = ''


def init(port=9274):
    global URL
    URL = f'http://localhost:{port}/lookup-application/api/search'


def get_entities(query: str, maxResults: int=None, minRelevance: int=None) -> list:
    parameters = {}
    parameters['query'] = query
    parameters['format'] = 'JSON'
    
    if maxResults:
        parameters['maxResults'] = maxResults
    if minRelevance:
        parameters['minRelevance'] = minRelevance

    response = requests.get(url=URL, params=parameters)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        return [doc['resource'][0] for doc in json_response['docs']]
    else:
        raise requests.exceptions.ConnectionError(f'{response.status_code}')


init()