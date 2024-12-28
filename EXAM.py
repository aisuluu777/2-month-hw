import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def get_stores(connection):
    sql = 'SELECT * FROM stores'
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def get_products_by_store(connection, store_id):
    query = '''SELECT p.title, c.title, p.unit_price, p.stock_quantity
               FROM products AS p
               INNER JOIN categories AS c ON p.category_code = c.code
               WHERE p.store_id = ?'''
    cursor = connection.cursor()
    cursor.execute(query, (store_id,))
    return cursor.fetchall()

def main():
    db_file = 'Test_data_base'
    connection = create_connection(db_file)
    if not connection:
        print('Ошибка подключения к базе данных.')
        return

    while True:
        print('Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, \n'
              'для выхода из программы введите цифру 0:')
        stores = get_stores(connection)

        if not stores:
            print('Магазины не найдены.')
            break

        for store in stores:
            print(f'{store[0]}. {store[1]}')

        try:
            store_id = int(input('Введите id магазина: '))
            if store_id == 0:
                break
        except ValueError:
            print('Пожалуйста, введите корректный id.')
            continue

        products = get_products_by_store(connection, store_id)
        if not products:
            print('Продукты не найдены или неверный id магазина.')
        else:
            for product in products:
                print(f'Название продукта: {product[0]}')
                print(f'Категория: {product[1]}')
                print(f'Цена: {product[2]}')
                print(f'Количество на складе: {product[3]}')
                print()

    connection.close()

if __name__ == '__main__':
    main()
