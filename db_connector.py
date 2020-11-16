import MySQLdb as mariadb
from db_credentials import host, user, pw, db

def connect_to_database(host = host, user = user, pw = pw, db = db):
    db_connection = mariadb.connect(host,user,pw,db)
    return db_connection

def execute_query(db_connection = None, query = None, query_params = ()):
    if db_connection is None:
        print("No connection to the database found")
        return None

    if query is None or len(query.strip()) == 0:
        print("Please pass a SQL query in query")
        return None

    cursor = db_connection.cursor()

    cursor.execute(query)

    db_connection.commit()
    return cursor

if __name__ == '__main__':
    db = connect_to_database()
    query = ""
    results = execute_query(db, query)