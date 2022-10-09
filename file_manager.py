import os
import shutil as sh

#Создаем файл
def create_file(name, text = None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)
    print(f'File {name} is created')

#Запись текста в файл
def fill_file(name, text = None):
    if text:
        with open(name, 'w') as f:
            f.write(text)
    else:
        with open(name, 'w') as f:
            f.write(input("Enter your text"))

#Считываем данные файла
def open_file(name):
    print(f'File {name} is opened')
    with open(name, 'r') as f:
        for line in f:
            print(line)

#Создаем папку
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('This folder already exists')
    print(f'Folder {name} created')

#Удаляем файл/папку
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)
    print(f'File {name} is deleted')

#Копируем файл/папку
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            sh.copytree(name, new_name)
        except FileExistsError:
            print('This folder already exists')
    else:
        sh.copy(name, new_name)
    print(f'File {name} is copied with name {new_name}')

#Переименовываем файл/папку
def rename_file(name, new_name):
    os.rename(name, new_name)
    print(f'File {name} is renamed as {new_name}')

#Перемещаемся в другую папку/понимаемся на уровень вверх
def move_directorty(name = '../'):
    if os.getcwd() == os.path.abspath(os.curdir):
        print('You are not allowed to leave from this folder')
    if name:
        os.chdir(name)
    print('Directory is changed')

#копируем файл в другую папку
def copy_filein(name, new_name, folder):
    copy_file(name, new_name)
    sh.move(new_name, folder)

#Перемещаем файл
def move_file(name, folder):
    sh.move(name, folder)
    print('File is moved')
