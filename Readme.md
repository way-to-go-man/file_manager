# Файловый менеджер
## Библиотеки:

При выполнении были использованы библиотеки os и shutil

    import os
    import shutil

А именно были использованы:

1. os.chdir(path) - смена текущей директории.

2. os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.

3. os.remove(path, *, dir_fd=None) - удаляет путь к файлу.

4. os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает файл или директорию из src в dst.

5. os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.

6. os.getcwd() - текущая рабочая директория.

7. os.path.isdir(path) - является ли путь директорией.

8. os.path.abspath(path) - возвращает нормализованный абсолютный путь.

9. shutil.copy(src, dst, follow_symlinks=True) - копирует содержимое файла src в файл или папку dst. Если dst является директорией, файл будет скопирован с тем же названием, что было в src. Функция возвращает путь к местонахождению нового скопированного файла.

10. shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False) - рекурсивно копирует всё дерево директорий с корнем в src, возвращает директорию назначения.

11. shutil.move(src, dst, copy_function=copy2) - рекурсивно перемещает файл или директорию (src) в другое место (dst), и возвращает место назначения.

## Функционал:

    def create_file(name, text = None): - создание файла
<br/>

    def fill_file(name, text = None): - заполнение файла
<br/>

    def open_file(name): - считывает данные файла
<br/>

    def create_folder(name): - создает папку
<br/>

    def delete_file(name): - удаляет файл/пустую папку
<br/>

    def copy_file(name, new_name, folder = None): - копирует файл/папку
<br/>

    def rename_file(name, new_name): - переименовывает файл/папку
<br/>

    def move_directorty(name = '../'): - выполняет переход между папками, при не заполнении name выполянет выход на уровень вверх
<br/>

    def copy_filein(name, new_name, folder): - копирует файл в дуругую папку
<br/>

    def move_file(name, folder): - перемещает файл в другую папку
<br/>
