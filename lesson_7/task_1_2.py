import os
from pathlib import Path


def create_file(directory, file_name):
    Path(f"{directory}\\{file_name}").touch()


def create_folder(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def add_folder_file(directory_path):
    if '.' in directory_path[-1]:                               # если в дальней папке есть файл
        file_name = directory_path[-1]                          # получаем имя файла
        directory_path = os.path.join(*directory_path[:-1])     # от пути к файлу отрезаем имя файла и преобразуем путь
        create_folder(directory_path)                           # создаем папку, передав путь
        create_file(directory_path, file_name)                  # создаем файл передав путь и имя файла
    else:                                                       # это если нужно создать только папку без файла
        directory_path = os.path.join(*directory_path)
        create_folder(directory_path)


def line_parse(content):
    directory_path = []                    # список-путь к новой папке
    for line in content:                   # запомним "место" названия папки в строке
        i = line.find('|--')               # далее на такое же место в "списке-пути" вставим имя папки
        if i//3 < len(directory_path):                  # если индекс (место) в списке-пути для новой папки существует
            directory_path[i//3] = line[i+3:]           # просто присвоим индексу новое значение
            directory_path = directory_path[:i//3+1]    # и обрежем все что после
        else:
            directory_path.insert(i//3, line[i+3:])     # если индекса нет, добавим его
        add_folder_file(directory_path)


with open('config.yaml', 'r') as file:
    line_parse(file.read().splitlines())
