from flask import Flask, request, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/results", methods=['GET'])
def get_results():

    # Get the data from the GET request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    location = request.args.get('location')
    term = request.args.get('term')
    limit = 5

    # Call Yelp API if latitude and longitude are provided
    if latitude:
        endpoint = "https://api.yelp.com/v3/businesses/search?term={}&latitude={}&longitude={}&limit={}".format(term, latitude, longitude, limit)

    # Call Yelp API for given location if latitude and logitude are not provided
    else:
        endpoint = "https://api.yelp.com/v3/businesses/search?term={}&location={}&limit={}".format(term, location, limit)
       
        
    headers = {"Authorization": "Bearer 04xem-7qB0W84jZs9uTYDsTUZj3gLJPthl5yi5IXqo_D0oLQ1He4ImOB5D5G3Vm9G9yGQ7V1YrfMewnqcrhFw5GgotlPjOMGUZ-P0ikPehTd5Y9IVA_NVLRreQJtX3Yx"}
    r = requests.get(url=endpoint, headers=headers)

    # Store Yelp search results
    search_results = r.json()

    # Check if businesses have been found
    if 'businesses' in search_results:
        limit = len(search_results['businesses'])

    # If no businesses have been found
    else:
        limit = 0
    
    # Initialize empty array for results
    # If no businesses are found, the empty array will be returned
    return_results = []

    # Get business names and ratings
    for i in range(0, limit):
        return_results.append({"business": search_results["businesses"][i]["name"], "rating": search_results["businesses"][i]["rating"]})

    return jsonify(return_results)


if __name__ == '__main__':
    app.run(port=5000)