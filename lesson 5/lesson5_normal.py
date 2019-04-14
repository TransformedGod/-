# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import lesson5_easy as func

def menu():
    while True:
        print("Меню:")
        print("1. Перейти в папку")
        print("2. Просмотреть содержимое текущей папки")
        print("3. Удалить папку")
        print("4. Создать папку")
        print("5. Выйти")
        answer = int(input("Введите номер ответа: "))

        if answer == 1:
            try:
                dir_path = input("Введите путь: ")
                os.chdir(dir_path)
                print("Успешно! Текущая папка: " + os.getcwd())
            except FileNotFoundError:
                print("Нет такой папки!")
                continue

        if answer == 2:
            func.view_dir()

        if answer == 3:
            try:
                path = input("Введите путь к папке: ")
                func.del_dir(path)
                print("Успешно! Папка удалена!")
            except FileNotFoundError:
                print("Нет такой папки!")
                continue

        if answer == 4:
            try:
                path = input("Введите путь к новой папке: ")
                func.cr_dir(path)
                print("Успешно! Папка создана!")
            except FileExistsError:
                print("Такая папка уже есть!")
                continue


        if answer == 5:
            break
menu()
