import os
import requests
import json


API_KEY = os.environ.get('startAPI')


# start.gg api endpoint
url = "https://api.start.gg/gql/alpha"

# GraphQL query 
query = """
query TournamentQuery($slug: String) {
    tournament(slug: $slug) {
        id
        name
        events {
            id
            name
        }
    }
}
"""


variables = {"slug": "tournament/evo-2023"}  # example slug

# Headers with authentication token
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"  # Ensure Bearer prefix
}


payload = {"query": query, "variables": variables}


try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for HTTP errors
    data = response.json()

    # Check for GraphQL errors, not really sure what happens if not here
    if "errors" in data:
        print("GraphQL Errors:")
        print(json.dumps(data["errors"], indent=2))
    else:
        # json format
        print(json.dumps(data, indent=2))

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error: {http_err}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as req_err:
    print(f"Request Error: {req_err}")