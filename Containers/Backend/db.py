import os
import mysql.connector as Connector
from mysql.connector import errorcode

def get_connection():
    try: 
        connection =  Connector.connect( user = os.environ.get('DATABSE_USER'),
                                        password = os.environ.get('DATABASE_PASSWORD'),
                                        database = os.environ.get('DATABASE_DB'),
                                        port = os.environ.get('DATABASE_PORT')
        )
    except connection.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password") #Ought to be replaced with some logging tool?
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return connection

def close_connection(conn):
    if conn is not None:
        conn.close()

def init_database():
    db = os.environ.get('DATABASE_DB')
    database_start_script = f"""
    CREATE DATABASE IF NOT EXISTS {db};
    USE {db};
    
    CREATE TABLE IF NOT EXIST ToDo
    (
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Status BOOL DEFAULT FALSE,
        Description TEXT
    );
    """
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(database_start_script, multi=True)
        cursor.fetchall()
    close_connection(conn=connection)