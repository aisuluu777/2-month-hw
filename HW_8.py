import sqlite3


def create_connection(hw_db):
    connection = None
    try:
        connection = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return connection

#
# def create_table(connection, create_table_countries_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_countries_sql)
#     except sqlite3.Error as e:
#         print(e)
#
#
#
# sql_countries_table = '''
#     CREATE TABLE countries (
#      c_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title  VARCHAR (200) NOT NULL
#     )'''
#
# def insert_countries(connection, title):
#     sql = '''INSERT INTO countries
#     (title)
#     VALUES (?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, (title,))
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# my_conn = create_connection('countries.db')
# if my_conn is not None:
#     print('Successfully connected to database')
#     create_table(my_conn, sql_countries_table)
#     insert_countries(my_conn, 'Kyrgyzstan')
#     insert_countries(my_conn, 'Italy')
#     insert_countries(my_conn, 'Germany')
#     my_conn.close()
#
# db_name = 'countries.db'
#
#
# def create_table(connection, create_table_cities_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_cities_sql)
#     except sqlite3.Error as e:
#         print(e)
#
#
# sql_cities_table = '''
#     CREATE TABLE cities (
#     ct_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title  VARCHAR (200) NOT NULL,
#     area FLOAT DEFAULT 0,
#     country_id INTEGER DEFAULT NULL
#     REFERENCES countries (c_id)
#
#     )'''
#
#
# def insert_cities(connection, title, area, country_id):
#     sql = '''INSERT INTO cities
#     (title, area, country_id)
#     VALUES (?,?,?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql,(title, area, country_id))
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
#
# my_conn = create_connection('cities.db')
# if my_conn is not None:
#     print('Successfully connected to database')
#     create_table(my_conn, sql_cities_table)
#     insert_cities(my_conn, 'Bishkek', 127 , 1)
#     insert_cities(my_conn, 'Osh', 182 , 1)
#     insert_cities(my_conn, 'Rome',1285 ,2)
#     insert_cities(my_conn, 'Milan',181.8,2)
#     insert_cities(my_conn, 'Sicily', 25711, 2)
#     insert_cities(my_conn, 'Stuttgart',207.4,3)
#     insert_cities(my_conn, 'Berlin', 891,3)
#     my_conn.close()
#
# db_name = 'cities.db'
#

def create_table(connection, create_table_students_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_students_sql)
    except sqlite3.Error as e:
        print(e)


sql_students_table = '''
    CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name  VARCHAR (200) NOT NULL,
    last_name  VARCHAR (200) NOT NULL,
    city_id INTEGER DEFAULT NULL
    REFERENCES cities (ct_id)

    )'''


def insert_students(connection, first_name, last_name, city_id):
    sql = '''INSERT INTO students
    (first_name, last_name, city_id)
    VALUES (?,?,?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (first_name, last_name, city_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


my_conn = create_connection('students.db')
if my_conn is not None:
    print('Successfully connected to database')
    create_table(my_conn, sql_students_table)
    insert_students(my_conn, 'Almaz', 'Jumabekov', 1)
    insert_students(my_conn, 'Mirlan', 'Asanov', 2)
    insert_students(my_conn, 'Aruuke', 'Kubatalieva', 1)
    insert_students(my_conn, 'Monica', 'Bellucci', 3)
    insert_students(my_conn, 'Kyle', 'Jenner', 4)
    insert_students(my_conn, 'Leonardo', 'Da vinci', 5)
    insert_students(my_conn, 'Claud', 'Monet', 6)
    insert_students(my_conn, 'Jim', 'Smith', 3)
    insert_students(my_conn, 'Emma', 'Stone', 5)
    insert_students(my_conn, 'Emilia', 'Shank', 6)
    insert_students(my_conn, 'Frank', 'Sinatra', 7)
    insert_students(my_conn, 'Arnold', 'Shwart', 7)
    insert_students(my_conn, 'Aisuluu', 'Nurlanova', 1)
    insert_students(my_conn, 'Aidai', 'Almazbekova', 2)
    insert_students(my_conn, 'Ralph', 'Loaran',2 )
    my_conn.close()

db_name = 'students.db'

def get_cities(connection):
    get ='''SELECT ct_id, title FROM cities'''
    cursor = connection.cursor()
    cursor.execute(get)
    return cursor.fetchall()
user_answer =int(input('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже,\n'
      'для выхода из программы введите 0:'))


def get_students_by_city(connection, city_id):
    query = ''' SELECT students.first_name, students.last_name, 
    countries.title, cities.title, cities.area 
    FROM students INNER JOIN cities ON students.city_id = cities.ct_id 
     WHERE cities.ct_id = ? '''
    cursor = connection.cursor()
    cursor.execute(query, (city_id,))
    return cursor.fetchall()

def main():
    connection = create_connection('students.db')
    if not connection:
        print('не удалось подключится к базе данных')
        return

    while True:
        print('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже,\n'
              ' для выхода из программы введите 0:')
        cities = get_cities(connection)
        if not cities:
            print('Произошла ошибка')
            break
        for city in cities:
            print(f'{city[0]}, {city[1]}')
        try:
            city_id = int(input('введите id города'))

        except ValueError:
            print('Произошла ошибка, пожалуйста попробуйте снова.')

        students = get_students_by_city(connection, city_id)
        if not students:
            print(f'В городе с id {city_id} нет учеников или неверный id.')

        else:
            print('\nСписок учеников:')
        for student in students: print(
            f'Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]},\n'
            f' Город: {student[3]}, Площадь города: {student[4]} км²')
        connection.close()

if __name__ == '__main__':
    main()