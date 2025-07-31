"""
Guilty Gear Strive next 7 days from select date 
"""

strive_query = """
query TournamentsByVideogame($perPage: Int!, $afterDate: Timestamp!, $beforeDate: Timestamp!) {
  tournaments(query: {
    perPage: $perPage
    page: 1
    sortBy: "startAt asc"
    filter: {
      videogameIds: [33945]
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

strive_variables = {
  "perPage": 10,
  "afterDate": 1753833600,
  "beforeDate": 1754524799
}

