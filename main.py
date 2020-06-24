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
            #successfully created the dictionary
    Stage 6
        Check the key value pairs against themselves for a future feature update
        ~UP~DATE~
        Store the key value pair of business names and business status.
            #done
        Rerun the program and check if business status has changed.
            -this requires reruning the API call and creation of a new file to
            re-parse through.
            #success
            #added checking of file and deletion of file so that data can be updated
        ~Do I store the data as a plaintext or as a python dict?
            Python dict allows me to update the entries
            Json file format as well
            Plain text does not
            Python cannot talk to json directly but has to be converted,
            so working with a python dict would be the path of least resistance.
            #stored as python file called status.py
            #figured out how to negate a function or file call in a conditional
            statement: use not.
        ~UP~DATE
            A dictionary containing all business names and status is created and
            written to status.py. I can now import this dict and check it against
            itself.
            Successfully import dict and test to see if all files are created/deleted
            correctly(check "First start")
                -Having trouble importing salon_status from another file
            #works 
    Stage 7
            #had to split up the stages because Stage 6 was the most difficult stage yet
        Check the imported values against the newest values from the newest API call

        Create a log beneath the dictionary that exists in status.py

'''

import json
import requests
import os.path
import os

with open('api_key.txt', 'r') as f:
    api_key = f.readline()

find_place = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
             + 'location=37.866530,-122.263210'
             + '&radius=1600'
             + '&keyword=hair%20cut'
             + '&key=' + api_key)


'''if os.path.exists('data.json'):
    os.remove('data.json')

with requests.get(find_place) as response:
    with open('data.json', 'w') as f:
        json.dump(response.json(), f, sort_keys=True, indent=4)

'''

with open('data.json', 'r') as f:
    response_dict = json.load(f)

if not os.path.exists('status.py'):
    salon_status={}
    for x in response_dict['results']:
        salon_status[x['name']] = x['business_status']
    with open('status.py', 'w') as f:
        f.write('salon_status= ')
        json.dump(salon_status, f, sort_keys=True, indent=4)
else:
    from status.py import salon_status
