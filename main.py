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


with requests.get(find_place) as response:
    with open('data.txt', 'w') as f:
        json.dump(response.json(), f, sort_keys=True, indent=4)
