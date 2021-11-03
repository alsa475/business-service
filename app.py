from flask import Flask, request
import json
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
def results():

    # Get the data from the POST request
    data = json.loads(request.data)
    term = data["category"]
    location = data["location"]
    limit = 5

    # Call Yelp API 
    endpoint = "https://api.yelp.com/v3/businesses/search?term={}&location={}&limit={}".format(term, location, limit)
    headers = {"Authorization": "Bearer 04xem-7qB0W84jZs9uTYDsTUZj3gLJPthl5yi5IXqo_D0oLQ1He4ImOB5D5G3Vm9G9yGQ7V1YrfMewnqcrhFw5GgotlPjOMGUZ-P0ikPehTd5Y9IVA_NVLRreQJtX3Yx"}
    r = requests.get(url=endpoint, headers=headers)

    # Store Yelp search results
    search_results = r.json()  

    # Get business names and ratings
    return_results = []
    for i in range(0,5):
        return_results.append({"business": search_results["businesses"][i]["name"], "rating": search_results["businesses"][i]["rating"]})

    return json.dumps(return_results)


if __name__ == '__main__':
    app.run(port=5000, debug=True)