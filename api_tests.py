
"""
Loops through calls and makes a GET request to test API calls
"""

import json
import requests

# TODO Place your access_token here!
access_token = ''

api_calls = ['users', 'groups', 'wishes', 'statuses', 'projects', 'sprints', 'stories', 'tasks']
api_url = 'http://localhost:8000/api'
headers = {'Authorization': 'Token %s' % access_token}

for item in api_calls:
    resp = requests.get(url='%s/%s/' % (api_url, item), headers=headers)

    print '=> list GET call of %s' % item
    print json.dumps(resp.json(), indent=4, sort_keys=True)