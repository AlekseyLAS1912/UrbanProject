import os

directory = 'C:\\Windows\\help'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        filesize = os.path.getsize(filepath)
        parentdir = os.path.dirname(filepath)
        print(f'''Файл: {filepath}, Время изменения файла: {filetime}, Размер файла: {filesize}, 
        Родительская дирректория: {parentdir}''')
