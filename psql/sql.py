import psycopg2 as pg
import os
from dotenv import load_dotenv
load_dotenv('../testing.env')
conn = pg.connect(host= os.getenv('host'), dbname = os.getenv('dbname'), user = os.getenv('user'), password = os.getenv('password'), port = os.getenv('port'))
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tourneys (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            time VARCHAR(255),
            url VARCHAR(255),
            checked BOOLEAN
            );""")



conn.commit()
cur.close()
conn.close()
