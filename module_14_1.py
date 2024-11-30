import sqlite3

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users_data = []
for i in range(1, 11):
    users_data.append((i, f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

cursor.executemany('INSERT INTO Users '
                   '(id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)', users_data)

connection.commit()

cursor.execute('''
UPDATE Users
SET balance = balance - 500
WHERE id % 2 = 1
''')

connection.commit()

cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 1
''')

connection.commit()

cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

connection.close()
