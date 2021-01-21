import requests
import json
import time
import os
import sys
from pathlib import Path  # Python 3.6+ only

from playsound import playsound
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")
USERS_TO_FOLLOW = ['Wario64', 'spieltimes', 'SOLELINKS']
SEARCH_TERMS = ['ps5', 'playstation', 'console', 'direct', 'PS ']
HEADERS = {
        "Content-type": "application/json",
        "Authorization": f'Bearer {TOKEN}'
    }


def run_setup():
    for user in USERS_TO_FOLLOW:
        body = {'add': [{'value': f'from:{user}'}]}
        response = requests.post('https://api.twitter.com/2/tweets/search/stream/rules', headers=HEADERS, json=body)
        if response.status_code != 200:
            print('Error setting up followees:', response.text)


def run_listener():
    print("Listening")
    while(True):
        with requests.get('https://api.twitter.com/2/tweets/search/stream', headers=HEADERS, stream=True) as r:
            for line in r.iter_lines():
                # filter out keep-alive new lines
                if line:
                    try:
                        decoded_line = line.decode('utf-8')
                        text = json.loads(decoded_line)['data']['text']
                        if any(search_term in text.lower() for search_term in SEARCH_TERMS) and not 'not a drop' in text.lower():
                            print(text)
                            print('*'*40)
                            playsound('./notification.mp3')
                    except KeyError:
                        pass
        time.sleep(.5)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_setup()
        run_listener()
    else:
        run_listener()
