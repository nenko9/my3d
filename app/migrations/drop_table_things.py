import psycopg2
import os

DB='postgresql://{}:{}@db:5432/my3d'.format(os.getenv('PGUSER'),os.getenv('PGPASSWORD'))

things="""
drop table if exists things;
"""

try:
    conn = psycopg2.connect(DB)
    with conn.cursor() as cursor:
        cursor.execute(things)
finally:
    conn.commit()
    conn.close()