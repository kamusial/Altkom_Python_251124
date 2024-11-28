import sqlite3

def read_entire_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('SELECT name FROM sqlite_master WHERE type="table";')
    tables = c.fetchall()
    database_content = {}
    for table in tables:
        table_name = table[0]
        c.execute(f'SELECT * FROM {table_name}')
        rows = c.fetchall()
        c.execute(f'PRAGMA TABLE_INFO({table_name})')
        columns = [column[1] for column in c.fetchall()]
        database_content[table_name] = {
            'columns': columns,
            'rows': rows
        }
    c.close()
    conn.close()

    return database_content

db_content = read_entire_database('results.db')
for table, content in db_content.items():
    print(f'Table: {table}')
    print(f'Columns: {content["columns"]}')
    print(f'Rows:')
    for row in content['rows']:
        print(row)
    print()