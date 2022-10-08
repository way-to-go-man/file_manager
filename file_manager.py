import os
import shutil as sh

#Создаем файл
def create_file(name, text = None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)
    print(f'File {name} is created')

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
def copy_file(name, new_name, folder = None):
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
    if name:
        os.chdir(name)
    print('Directory is changed')

#копируем файл в другую папку
def copy_filein(name, new_name, folder):
    copy_file(name, new_name)
    sh.move(new_name, folder)





if __name__ == '__main__':
    create_file('text.txt', 'Hello World!!!')
    create_folder('folder')
    copy_filein('text.txt', 'text1.txt','folder')