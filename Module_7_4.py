import os
import time
os.chdir(r'D:\Urban')
for root, dirs, files in os.walk(r'D:\Urban'):
    os.chdir(root)
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.split(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir[0]}')