'''
    Stage 1
        Receive a json page when requesting google places API
            #SUCCESS. I receive a json page when posting a get request through
            my web browser. The return is a json page with my completed search
            query
    Stage 2
        Set up search criteria 
'''

api_key = 'AIzaSyARrE3VPSm9UHGHVu4VY7DuzxQBtOtXst0'

find_place = https://maps.googleapis.com/maps/api/place/nearbysearch/json?
             location=37.866530,-122.263210
             &radius=1600
             &keyword=hair%20cut
             &key=api_key
