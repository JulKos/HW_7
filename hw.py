import os
import json
from pprint import pprint

def create_dict(file_name: str) -> dict:
    result: dict = dict()
# Вывод словаря

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            dishes_name = line.strip()
            records_quantity = int(file.readline())
            ingredients_list = []
            for ingredient in range(records_quantity):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredients_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure}
                )
                result[dishes_name] = ingredients_list
            file.readline()
    return result


cook_book = create_dict("recipes.txt")
pprint(cook_book)


def get_shop_list_by_dishes(person_count, *dishes):
    shop_dict = {}
    shop_list_result = []

    for dish in dishes:
        if dish in cook_book.keys():
            l = cook_book.get(dish)
            for ingredients in l:
                shop_dict.update(
                    {ingredients['ingredient_name']: {'measure': ingredients['measure'], 'quantity': (ingredients['quantity']) * person_count}}
                )

    pprint(shop_dict)


get_shop_list_by_dishes(2, 'Запеченный картофель', 'Омлет')


def dict_create(*file_name):
# читает содержимое входящих файлов txt,
# подсчитывает количество строк в файлах, создает словарь, где ключ - имя файла,
# значение - количество строк и содержимое файла.


    res_file = {}
    for files in file_name:
        try:
            with open(files, encoding='utf-8') as file:
                contents = file.read()
        except FileNotFoundError:
            print(f'К сожалению, {files} не найден!')
        else:
            line_count = 0
            result_file_dict = {}
            for line in open(files, encoding='utf-8'):
                line_count += 1
            result_file_dict.update(
                {files: [line_count, contents]}
            )
            res_file.update(result_file_dict)
    return res_file


dict_create('1.txt', '2.txt', '3.txt')


def sorted_data():
# Сортирует данные для последующей записи

    files_to_sorted = dict_create('1.txt', '2.txt', '3.txt')
    sorted_data = sorted(files_to_sorted.values())
    for i in sorted_data:
        sorted_dict = {}
        for k in files_to_sorted.keys():
            if files_to_sorted[k] == i:
                sorted_dict[k] = files_to_sorted[k]
                pprint(sorted_dict)

sorted_data()

def dump_new_file():
# Записывает содержимое входящих файлов в новый файл, открывает новый файл на чтение.

    file_to_save = sorted_data()
    with open('test_file', 'w', encoding='utf-8') as new_f:
        json.dump(file_to_save, new_f)
    with open('test_file') as data_file:
        data_loaded = json.load(data_file)
    return data_loaded


dump_new_file()
