# 33945 guilty gear strive game ID

import os
import requests
import json
from . import queries as q  

API_KEY = os.environ.get('startAPI')

def start_tourneys():
    result = {}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # Ensure Bearer prefix
    }

    payload = q.tourney_list_query(q.STRIVE, period = q.SEVEN_DAYS)
    # start.gg api endpoint
    url = "https://api.start.gg/gql/alpha"

    try:
        response = requests.post(url, json= payload, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        # Check for GraphQL errors, not really sure what happens if not here
        if "errors" in data:
            print("GraphQL Errors:")
            result = json.dumps(data["errors"], indent=2)
            print(result)
            return result
        else:
            # json format
            result = data['data']['tournaments']['nodes']
            #print(result)
            return result

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
        print(f"Response: {response.text}")
        return response.text
    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")
        return req_err

# data = start_tourneys()
# for i in data:
#     print(i['name'])
# gameIDquery = """
# query VideogameByName($name: String!) {
#   videogames(query: {
#     filter: {
#       name: $name
#     }
#   }) {
#     nodes {
#       id
#       name
#     }
#   }
# }
# """

# gameIDvariables = {'name': 'Guilty Gear -Strive-'}
# gameIDpayload = {"query": gameIDquery, "variables": gameIDvariables}

# try:
#     response = requests.post(url, json= gameIDpayload, headers=headers)
#     response.raise_for_status()  # Raise exception for HTTP errors
#     data = response.json()

#     # Check for GraphQL errors, not really sure what happens if not here
#     if "errors" in data:
#         print("GraphQL Errors:")
#         print(json.dumps(data["errors"], indent=2))
#     else:
#         # json format
#         print(json.dumps(data, indent=2))

# except requests.exceptions.HTTPError as http_err:
#     print(f"HTTP Error: {http_err}")
#     print(f"Response: {response.text}")
# except requests.exceptions.RequestException as req_err:
#     print(f"Request Error: {req_err}")