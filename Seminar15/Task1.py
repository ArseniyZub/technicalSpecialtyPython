import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_directory(path):
    try:
        with open('directory_contents.txt', 'w') as output_file:
            for root, dirs, files in os.walk(path):
                for directory in dirs:
                    directory_path = os.path.join(root, directory)
                    directory_info = FileInfo(os.path.basename(directory_path), '', True, os.path.basename(root))
                    
                    output_file.write(str(directory_info) + '\n')
                    logging.info(f'Directory: {directory_info}')

                for file in files:
                    file_path = os.path.join(root, file)
                    name, extension = os.path.splitext(file)
                    file_info = FileInfo(name, extension, False, os.path.basename(root))
                   
                    output_file.write(str(file_info) + '\n')
                    logging.info(f'File: {file_info}')
    except Exception as e:
        logging.error(f'Error: {str(e)}')



if __name__ == '__main__':
    directory_path = input("Введите путь до директории: ")
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        process_directory(directory_path)
    else:
        print("Указанный путь не существует или не является директорией.")