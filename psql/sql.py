import psycopg2 as pg
import os, sys
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.api import start_tourneys
# from api import challonge

from datetime import datetime, timedelta
#loading from env, not sure what service ill use yet
load_dotenv('../testing.env')

#conn and cur using env
conn = pg.connect(host= os.getenv('host'), dbname = os.getenv('dbname'), user = os.getenv('user'), password = os.getenv('password'), port = os.getenv('port'))
cur = conn.cursor()

cur.execute("""--sql
            CREATE TABLE IF NOT EXISTS tourneys (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            time VARCHAR(255),
            url VARCHAR(255),
            isonline BOOLEAN,
            checked BOOLEAN
            );""")
conn.commit()


def startgg_check():
    start_data = start_tourneys()  # expects a list of dicts
    insert_sql = """--sql
        INSERT INTO tourneys (id, name, time, url, isonline, checked)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """
    for i in start_data:
        tid = str(i['id'])  # ensure string to match VARCHAR column type
        name = i['name']
        time_str = datetime.fromtimestamp(int(i['startAt'])).strftime('%Y-%m-%d %H:%M')
        url = f"https://www.start.gg/{i['slug']}" #idk if theres a better way, seems probe to injections
        isonline = bool(i.get('isOnline', True))  # default True if key missing
        checked = True

        cur.execute(insert_sql, (tid, name, time_str, url, isonline, checked))
    conn.commit()

def challonge_check():
    pass


startgg_check()


cur.close()
conn.close()

