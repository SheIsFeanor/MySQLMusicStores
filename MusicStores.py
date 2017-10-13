# coding: utf-8

import mysql.connector
from mysql.connector import Error


def connect():
    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'MusicStores', user = 'root', password = '35689226') 
        if conn.is_connected():
            print("Соединение с базой данных MusicStores установлено\n"
                  ".\n"                   
                  ".\n"                   
                  ".")
            
    except Error as e:
        print(e)
    
    finally:
        return conn


def main():
    connection = connect()
    cursor = connection.cursor()
    user_choice = -1
    while user_choice != 0: # до тех пока пользователь не решит выйти из базы данных, крутим меню
        user_choice = menu(connection, cursor)


def menu(conn, curs):
    print("--------База данных сети музыкальных магазинов--------\n"           
          "| Выберите действие:\n"           
          "| 1 - Вывести список доступных таблиц\n"           
          "| 2 - Просмотр содержимого таблицы\n"           
          "| 3 - Вставка строки в таблицу\n"           
          "| 4 - Удаление строк при помощи WHERE\n"           
          "| 5 - Упорядочивание строк при помощи ORDER BY\n"           
          "| 0 - Выход\n"           
          "------------------------------------------------------\n")
    choice = int(input())
    
    if choice == 1: # Вывод списка доступных таблиц
        print("---\n"               
              "Список доступных таблиц:")
        curs.execute("SHOW TABLES")
        rows = curs.fetchall()
        for row in rows:
            print("- ", str(row)[2:len(row) - 4])
        
        print("---\n")
        return 1
    
    elif choice == 2: # Просмотр содержимого таблицы
        print("---")
        name_table = table_choice()
        if name_table == 0:
            return 2
        print("|", end = ' ')
        curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '" + name_table + "'")
        rows = curs.fetchall()
        for row in rows:
            print(str(row)[2:len(row) - 4], end = ' | ')
        print('\n-------------------------------------------------------------------------------------------------------')
        curs.execute("SELECT * FROM `MusicStores`.`" + name_table + "`")
        rows = curs.fetchall()
        for row in rows:
            print(row)
        print("---\n")
        return 2
        
    elif choice == 3: # Вставка строки в таблицу
        print("---")
        name_table = table_choice()
        if name_table == 0:
            return 3
        print("Данные представлены в следующем виде:")
        curs.execute("SELECT * FROM `MusicStores`.`" + name_table + "` LIMIT 1")
        rows = curs.fetchall()
        for row in rows:
            print(row)
        print("\nВведите вставляемые значения или напишите Назад для выхода в главное меню:")
        values = str(input())
        if values == "Назад":
            print('\n')
            return 3
        curs.execute("INSERT INTO `MusicStores`.`" + name_table + "` VALUES " + values)
        conn.commit()
        print("---\n")
        return 3
    
    elif choice == 4: # Удаление строк по правилу WHERE
        print("---")
        name_table = table_choice()
        if name_table == 0:
            return 4
        print("|", end = ' ')
        curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '" + name_table + "'")
        rows = curs.fetchall()
        for row in rows:
            print(str(row)[2:len(row) - 4], end = ' | ')
        print('\n-------------------------------------------------------------------------------------------------------')
        curs.execute("SELECT * FROM `MusicStores`.`" + name_table + "`")
        rows = curs.fetchall()
        for row in rows:
            print(row)
        print("\nВведите условие или напишите Назад для выхода в главное меню:")
        condition = str(input())
        if condition == "Назад":
            print('\n')
            return 4
        curs.execute("DELETE FROM `MusicStores`.`" + name_table + "` WHERE " + condition)
        conn.commit()
        print("---\n")
        return 4
    
    elif choice == 5: # Упорядочивание строк при помощи ORDER BY
        print("---")
        name_table = table_choice()
        if name_table == 0:
            return 5
        print("|", end = ' ')
        curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '" + name_table + "'")
        rows = curs.fetchall()
        for row in rows:
            print(str(row)[2:len(row) - 4], end = ' | ')
        print('\n-------------------------------------------------------------------------------------------------------')
        curs.execute("SELECT * FROM `MusicStores`.`" + name_table + "`")
        rows = curs.fetchall()
        for row in rows:
            print(row)
        print("\nВведите названия столбцов для упорядочивания или напишите Назад для выхода в главное меню:")
        order = str(input())
        if order == "Назад":
            print('\n')
            return 5
        curs.execute("SELECT * FROM `MusicStores`.`" + name_table + "` ORDER BY " + order)
        rows = curs.fetchall()
        for row in rows:
            print(row)
        print("---\n")
        return 5
        
    elif choice == 0:
        print('Exit...')
        curs.close()
        conn.close()
        return 0
    
    else:
        print("Такого действия не существует, попробуйте ещё раз!\n")
        return -1


def table_choice():
        flag = 1
        print("Выберите название таблицы:\n"               
              "1 - Покупатель\n"               
              "2 - Чек\n"               
              "3 - Магазин\n"               
              "4 - Поставщик\n"               
              "5 - Товар на складе\n"               
              "6 - Поставка\n"               
              "7 - Диск\n"               
              "8 - Гитара\n"               
              "9 - Аксессуар\n"               
              "0 - Назад\n")
               
        while flag:
            num_table = int(input())
            if num_table == 1: return "Покупатель"
            elif num_table == 2: return "Чек"
            elif num_table == 3: return "Магазин"
            elif num_table == 4: return "Поставщик"
            elif num_table == 5: return "Товар_на_складе"
            elif num_table == 6: return "Поставка"
            elif num_table == 7: return "Диск"
            elif num_table == 8: return "Чек"
            elif num_table == 9: return "Аксессуар"
            elif num_table == 0: return 0
            else: print("Неккоректный выбор таблицы, введите ещё раз") 


main()
