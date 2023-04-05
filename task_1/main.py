"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!

os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
"""
import os
import re
import fnmatch
import csv


def get_catalog_files(mask):  # Получить список файлов по маске
    files_in_dir = os.listdir('.')
    list_files = []
    for file in files_in_dir:
        if fnmatch.fnmatch(file, mask):
            list_files.append(file)  # Добавление удовлетворяющегг условию файла в список
    return list_files


def get_info(mask, headers):
    list_files = get_catalog_files(mask)
    result_data = [headers]
    number_file = 1
    for file in list_files:
        result_line = [str(number_file)]
        with open(file, 'r') as active_file:
            data_from_file = active_file.read()
        for item in headers:
            os_prod_reg = re.compile(rf'{item}:\s*\S*')
            result_line.append(os_prod_reg.findall(data_from_file)[0].split()[2])
        result_data.append(result_line)
        number_file += 1
    return result_data


def build_report_to_csv(mask, headers, file_name):
    report_data = get_info(mask, headers)
    with open(file_name, 'w', encoding='utf-8', newline='') as report:
        file_writer = csv.writer(report)
        file_writer.writerows(report_data)


pattern = 'info_*.txt'
headers_report = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
build_report_to_csv(pattern, headers_report, 'data_report.csv')
