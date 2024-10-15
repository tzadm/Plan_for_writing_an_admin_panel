import sqlite3


def initiate_db():
    connection_telegram_db = sqlite3.connect('not_telegram__3.db')
    cursor = connection_telegram_db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
    (ID INTEGER PRIMARY KEY,
     title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection_telegram_db.commit()
    connection_telegram_db.close()

def get_all_products():
    connection_telegram_db = sqlite3.connect('not_telegram__3.db')
    cursor = connection_telegram_db.cursor()
    cursor.execute('SELECT * FROM Products')
    product_list = cursor.fetchall()
    connection_telegram_db.commit()
    connection_telegram_db.close()
    return product_list


# connection_telegram_db = sqlite3.connect('not_telegram__3.db')
# cursor = connection_telegram_db.cursor()
# for i in range(0, 4):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES ( ?, ?, ?)',
#                    (f'Продукт {i + 1}', f'Описание {i + 1}', (i+1) * 100))
# connection_telegram_db.commit()
# connection_telegram_db.close()


print(get_all_products())
