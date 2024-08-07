from contextlib import contextmanager
import sqlite3

@contextmanager
def database_connection(db_name):
    connection = sqlite3.connect(db_name)
    try:
        yield connection
    finally:
        connection.close()

# Usage
with database_connection('example.db') as conn:
    cursor = conn.cursor()
    # cursor.execute('create table my_table(user varchar(50) primary key, address varchar(100))')
    cursor.execute("insert into my_table values ('arun', 'Bangalore')")
    cursor.execute('SELECT * FROM my_table')
    results = cursor.fetchall()
    print(results)
# Connection is automatically closed after the with block
