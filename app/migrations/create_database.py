import os


import os
import psycopg2

DB='postgresql://{}:{}@db:5432'.format(os.getenv('PGUSER'),os.getenv('PGPASSWORD'))
create_db="""
create database my3d;
"""
try:
    conn = psycopg2.connect(DB)
    with conn.cursor() as cursor:
        cursor.execute(create_db)
finally:
    if conn:
        conn.close()


