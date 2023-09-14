# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

def split_path(path):
    filename = os.path.basename(path)
    name, extension = os.path.splitext(filename)
    
    directory = os.path.dirname(path)
    
    return directory, name, extension

file_path = "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\bin\pycharm.exe"
result = split_path(file_path)
print(result)