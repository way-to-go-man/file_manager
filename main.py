from file_manager import *
import sys

command = sys.argv[1]

if command == 'createfile':
    name = sys.argv[2]
    text = sys.argv[3]
    create_file(name, text)

if command == 'fillfile':
    name = sys.argv[2]
    fill_file(name)

if command == 'openfile':
    name = sys.argv[2]
    open_file(name)

if command == 'createfolder':
    name = sys.argv[2]
    create_folder(name)

if command == 'deletefile':
    name = sys.argv[2]
    delete_file(name)

if command == 'copyfile':
    name = sys.argv[2]
    new_name = sys.argv[3]
    copy_file(name, new_name)

if command == 'renamefile':
    name = sys.argv[2]
    new_name = sys.argv[3]
    rename_file(name, new_name)

if command == 'move':
    name = sys.argv[2]
    move_directorty(name)

if command == 'copyfilein':
    name = sys.argv[2]
    new_name = sys.argv[3]
    folder = sys.argv[4]
    copy_filein(name, new_name, folder)

if command == 'movefile':
    name = sys.argv[2]
    folder = sys.argv[3]
    move_file(name, folder)