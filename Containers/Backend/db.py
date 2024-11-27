import os
import mysql.connector as Connector
from mysql.connector import errorcode
from flask import current_app, g

def get_connection(set_autocommit = False):
    with current_app.app_context():
        try: 
            g.db =  Connector.connect( host = os.environ.get('DATABASE_HOST'), 
                                            user = os.environ.get('DATABSE_USER'),
                                            password = os.environ.get('DATABASE_PASSWORD'),
                                            database = os.environ.get('DATABASE_DB'),
                                            port = os.environ.get('DATABASE_PORT')
            )
        except Connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password") #Ought to be replaced with some logging tool?
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        if (set_autocommit):
            g.db.autocommit = set_autocommit
        
        return g.db

def close_connection(conn):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_database():
    print("Initializing database...")
    init_table = """
    CREATE TABLE IF NOT EXISTS ToDo
    (
        ID INTEGER NOT NULL AUTO_INCREMENT,
        status BOOL NOT NULL DEFAULT FALSE,
        description TEXT,
        PRIMARY KEY (ID)
    );
    """
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(init_table, multi=True)
        cursor.fetchall()
    close_connection(conn=connection)