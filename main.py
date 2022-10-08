from file_manager import *
import sys

command = sys.argv[1]

if command == 'create file':
    name = sys.argv[2]
    create_file(name)

if command == 'fill file':
    text = sys.argv[3]
    fill_file(name, text)

if command == 'open file':
    name = sys.argv[2]
    open_file(name)

if command == 'create folder':
    name = sys.argv[2]
    create_folder(name)

if command == 'delete file':
    name = sys.argv[2]
    delete_file(name)

if command == 'copy file':
    name = sys.argv[2]
    new_name = sys.argv[3]
    copy_file(name, new_name)

if command == 'rename file':
    name = sys.argv[2]
    new_name = sys.argv[3]
    rename_file(name, new_name)

if command == 'move':
    name = sys.argv[2]
    move_directorty(name)

if command == 'copy file in':
    name = sys.argv[2]
    new_name = sys.argv[3]
    folder = sys.argv[4]
    copy_filein(name, new_name, folder)

if command == 'move file':
    name = sys.argv[2]
    folder = sys.argv[3]
    move_file(name, folder)