# import sqlite3
#
#
# def create_connection(hw_db):
#     connection = None
#     try:
#         connection = sqlite3.connect(hw_db)
#     except sqlite3.Error as e:
#         print(e)
#     return connection
#
#
# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)
#
#
#
# sql_products_table = '''
#     CREATE TABLE products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title_products  VARCHAR (200) NOT NULL,
#     price REAL NOT NULL DEFAULT 0.0,
#     quantity INTEGER NOT NULL DEFAULT 0
#     )'''
#
# def insert_products(connection, products):
#     sql = '''INSERT INTO products
#     ( title_products, price,quantity)
#     VALUES (?, ?, ?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, products)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
#
# my_conn = create_connection('products.db')
# if my_conn is not None:
#     print('Successfully connected to database')
#     create_table(my_conn, sql_products_table)
#     insert_products(my_conn, ('air conditioner', 5000, 10))
#     insert_products(my_conn, ('soap dove', 200, 10))
#     insert_products(my_conn, ('laptop lenovo', 40000, 5))
#     insert_products(my_conn, ('laptop acer', 45000, 23))
#     insert_products(my_conn, ('phonecase', 500, 35))
#     insert_products(my_conn, ('shampoo', 700, 25))
#     insert_products(my_conn, ('charger', 1000, 40))
#     insert_products(my_conn, ('headphone', 5000, 5))
#     insert_products(my_conn, ('fridge LG', 35000, 3))
#     insert_products(my_conn, ('fridge Samsung', 50000, 11))
#     insert_products(my_conn, ('kettle', 3000, 23))
#     insert_products(my_conn, ('microphone', 5000, 20))
#     insert_products(my_conn, ('lamp', 30000, 15))
#     insert_products(my_conn, ('doll', 2000, 100))
#
#     my_conn.close()
#
# db_name = 'products.db'
#
# def update_products_quantity(hw_db,quantity, id):
#     sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
#     try:
#         with sqlite3.connect(hw_db) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (quantity, id))
#             connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
#
# def update_products_price(hw_db, price, id):
#     sql = '''UPDATE products SET price = ? WHERE id = ?'''
#     try:
#         with sqlite3.connect(hw_db) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (price, id))
#             connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# def delete_products(hw_db, id):
#     sql = '''DELETE FROM products WHERE id = ?'''
#     try:
#         with sqlite3.connect(hw_db) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (id,))
#             connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# def select_products(hw_db):
#         sql = '''SELECT * FROM products'''
#         try:
#             with sqlite3.connect(hw_db) as connection:
#                 cursor = connection.cursor()
#                 cursor.execute(sql)
#                 rows = cursor.fetchall()
#                 for row in rows:
#                     print(row)
#         except sqlite3.Error as e:
#             print(e)
#
# def select_by_price(hw_db, price, quantity):
#     sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
#     try:
#         with sqlite3.connect(hw_db) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (price, quantity))
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
# def find_by_name(hw_db, name):
#     sql = '''SELECT * FROM products WHERE title_products LIKE ?'''
#     try:
#         with sqlite3.connect(hw_db) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, ('%' + name + '%',))
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
# find_by_name(db_name ,'a')
# delete_products(db_name,12)
# select_by_price(db_name,1000 , 10)
# update_products_quantity(db_name,25000 , 10)
# update_products_price(db_name,6000 , 1)
# select_products(db_name)
#
#
