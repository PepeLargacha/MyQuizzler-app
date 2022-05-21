import requests

URL = 'https://opentdb.com/api.php'
parameters = {
    'amount': 10,
    'type': 'boolean',
    'difficulty': 'medium',
}


def trivia_api_get():
    with requests.get(url=URL, params=parameters) as response:
        response.raise_for_status()
        question_data = response.json()['results']
        return question_data