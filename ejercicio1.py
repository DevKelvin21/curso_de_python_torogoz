import requests
import json

URL='https://scrapepark.org/courses/spanish/'

response=requests.get(URL)

print(f'Data: {response.text}')