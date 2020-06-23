'''
    Stage 1
        Receive a json page when requesting google places API
            #SUCCESS. I receive a json page when posting a get request through
            my web browser. The return is a json page with my completed search
            query
    Stage 2
        Set up search criteria
    Stage 3
        Store search results locally
            #fixed the format of find_places object. Had to concatenate the string
            using parenthesis and '+'
            #created a separate text file to store the API_key instead of keeping
            it within the same file. Adds security.
            #SUCCESS. Received JSON response and downloaded to local machine.
            -fix data formatting on local machine
    Stage 4
        Fix format of locally stored json data
            #done. Added parameters sort_keys=True and indent=4 to json.dump
            -successfully parse the data
            #changed json data stored locally into a json file for easier
            conversion/deconversion. Makes sense, more file nativity.
            #successfully accessed data through json.load and created a python
            dict object.
            #figured out how to parse json data
            #SUCCESS
    Stage 5
        Create a dict with business names and their business status as a key_value
        pair and store them locally.
    Stage 6
        Check the key value pairs against themselves for a future feature update

'''

import json
import requests

with open('api_key.txt', 'r') as f:
    api_key = f.readline()

find_place = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
             + 'location=37.866530,-122.263210'
             + '&radius=1600'
             + '&keyword=hair%20cut'
             + '&key=' + api_key)


'''with requests.get(find_place) as response:
    with open('data.json', 'w') as f:
        json.dump(response.json(), f, sort_keys=True, indent=4)
'''

with open('data.json', 'r') as f:
    dict = json.load(f)

for x in dict['results']:
    print(json.dumps(x['name']))
    print(json.dumps(x['business_status']))
