"""
Guilty Gear Strive next 7 days from select date 
"""
from datetime import datetime, timedelta

STRIVE = '33945'
STREET = ''
TEKKEN = ''
SEVEN_DAYS = 604800 # amount of seconds for seven days
ONE_DAY = 86400

"""
List of tourneys for the next seven days from specified start time, default is current time UTC
"""
def tourney_list_query(id, start = int(datetime.now().timestamp()), period = SEVEN_DAYS):
    
    query = """
        query TournamentsByVideogame($videogameIds: [ID!]!, $afterDate: Timestamp!, $beforeDate: Timestamp!) {
        tournaments(query: {
            perPage: 10
            page: 1
            sortBy: "startAt asc"
            filter: {
            videogameIds: $videogameIds
            hasOnlineEvents: true
            afterDate: $afterDate
            beforeDate: $beforeDate
            }
        }) {
            nodes {
            id
            name
            slug
            startAt
            endAt
            isOnline
            numAttendees
            events {
                id
                name
                    }
                }
            }
        }
        """

    variables = {
    "videogameIds": [id],
    "afterDate": start,
    "beforeDate": start + period
    }

    payload = {"query": query, "variables": variables}
    return payload

