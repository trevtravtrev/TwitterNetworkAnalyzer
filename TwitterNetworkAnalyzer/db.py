import sqlite3


def get_connection(db):
    return sqlite3.connect(db)


def get_cursor(connection):
    return connection.cursor()


def create_summary_table(cursor):
    return cursor.execute('''CREATE TABLE summary IF NOT EXISTS (date text, network text, followers integer, tweets integer)''')


def create_accounts_table(cursor):
    return cursor.execute('''CREATE TABLE accounts IF NOT EXISTS (date text, network text, account text, followers integer, tweets integer)''')


def insert_summary_row(cursor, date, network, followers, tweets):
    return cursor.execute(f"INSERT INTO summary VALUES ('{date}','{network}','{followers}','{tweets}')")


def insert_accounts_row(cursor, date, network, account, followers, tweets):
    return cursor.execute(f"INSERT INTO accounts VALUES ('{date}','{network}','{account}','{followers}','{tweets}')")


def save_and_close(connection):
    connection.commit()
    connection.close()
