
import json
import requests

##
# TODO: Fill in your superuser credentials!
##

username = ''
password = ''

"""
Global settings
"""

api_url = 'http://localhost:8000/api'

"""
Retrieve token from username/password combination POST
"""

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
parameters = {
    'username': username,
    'password': password
}
resp = requests.post(url='%s/token/' % api_url, data=json.dumps(parameters), headers=headers)
if 'token' not in resp.json():
    print "\n=> Please provide the script with an username and password to retrieve the access token!"
    exit()

access_token = resp.json()['token']

"""
PRINT retrieved access token
"""

print "\nRetrieved access token (KEY): %s" % access_token

"""
Loops through calls and makes a GET request to test each API call
"""


api_calls = ['users', 'groups', 'wishes', 'statuses', 'projects', 'sprints', 'stories', 'tasks']
headers = {'Authorization': 'Token %s' % access_token}

for item in api_calls:
    resp = requests.get(url='%s/%s/' % (api_url, item), headers=headers)

    print '\n=> Retrieve GET call of %s\n' % item
    print json.dumps(resp.json())
    # print json.dumps(resp.json(), indent=4, sort_keys=True)