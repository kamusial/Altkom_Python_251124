import mysql.connector

# Połączenie z bazą danych
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)
c = conn.cursor()

# Tworzenie tabeli
c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)
          ''')

# Wstawianie danych
c.execute('''
          INSERT INTO users (name, age)
          VALUES (%s, %s)
          ''', ('John Doe', 30))

c.execute("UPDATE users SET age = 31 WHERE name = 'John Doe'")

# Zatwierdzanie zmian
conn.commit()

# Pobieranie danych
c.execute('SELECT * FROM users')
print(c.fetchall())

# Zamknięcie połączenia
conn.close()
