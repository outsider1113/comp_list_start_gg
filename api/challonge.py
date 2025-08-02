import cloudscraper 
import json
import time
from datetime import datetime

# CLOUDFLAREREERERER
def scrape_tournaments(game_id='231004', per_page=5, max_pages=1):
    tournaments = []
    scraper = cloudscraper.create_scraper()  
    
    current_date = datetime.now()
    
    page = 1
    while page <= max_pages:
        url = f'https://challonge.com/search/tournaments.json?q=&page={page}&per={per_page}&filters%5Bgame_id%5D={game_id}'
        response = scraper.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if 'collection' not in data or not data['collection']:
                break
            for tournament in data['collection']:
                details = tournament.get('details', [])
                created_date_str = details[3].get('text') if len(details) > 3 else 'N/A'
                participants_str = details[1].get('text') if len(details) > 1 else 'N/A'
                
                tournaments.append({
                    'name': tournament.get('name', 'N/A'),
                    'created_date': created_date_str,
                    'link': tournament.get('link', 'N/A'),
                    'participants': participants_str
                })
            page += 1
            time.sleep(1.5)  # Rate limit (maybe make longer if saving info in DB)
        else:
            print(f"Error on page {page}: {response.status_code} - {response.text}")
            break
    
    return tournaments

results = scrape_tournaments()
print(json.dumps(results, indent=4)) 