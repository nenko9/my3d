import psycopg2
import os

DB='postgresql://{}:{}@db:5432/my3d'.format(os.getenv('PGUSER'),os.getenv('PGPASSWORD'))


# t_drop_things="""
# drop table if exists things;
# """

things="""
create table if not exists things(id integer, title text, url text);
"""

try:
    conn = psycopg2.connect(DB)
    with conn.cursor() as cursor:
        cursor.execute(things)
finally:
    conn.commit()
    conn.close()