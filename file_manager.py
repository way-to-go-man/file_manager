import os
import shutil as sh

def create_file(name, text = None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)
        print('File created')

def create_folder(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('This folder already exists')

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            sh.copytree(name, new_name)
        except FileExistsError:
            print('This folder already exists')
    else:
        sh.copy(name, new_name)

if __name__ == '__main__':
    create_file('text.txt')
    create_file('text.txt', 'some text')
    create_folder('somefolder')
    create_folder('somefolder')
    delete_file('text.dat')
    delete_file('somefolder')