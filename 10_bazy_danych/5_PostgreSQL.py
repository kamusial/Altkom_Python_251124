# Psycopg2 jest dedykowany tylko dla PostgreSQL.

import psycopg2

# Połączenie z bazą danych
conn = psycopg2.connect(
    dbname="yourdatabase",
    user="yourusername",
    password="yourpassword",
    host="localhost"
)
c = conn.cursor()

# Tworzenie tabeli
c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (id SERIAL PRIMARY KEY, name VARCHAR(255), age INT)
          ''')

# Wstawianie danych
c.execute('''
          INSERT INTO users (name, age)
          VALUES (%s, %s)
          ''', ('John Doe', 30))

# Zatwierdzanie zmian
conn.commit()

# Pobieranie danych
c.execute('SELECT * FROM users')
print(c.fetchall())

# Zamknięcie połączenia
conn.close()
