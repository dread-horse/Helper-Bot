import psycopg2
from data.config import *

def connect():
    conn = psycopg2.connect("dbname={0} user={1} password={2}".format(dbName, dbUser, dbPassword))

    cursor = conn.cursor()

    return conn, cursor
