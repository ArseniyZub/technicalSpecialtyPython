import os

def rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range):
    if not os.path.exists(directory):
        print(f"Директория {directory} не существует.")
        return

    files = [i for i in os.listdir(directory) if i.endswith(source_extension)]

    for i, filename in enumerate(files, start=1):
        original_name = os.path.splitext(filename)[0]
        
        if name_range and len(name_range) == len(original_name):
            name_part = original_name[name_range[0] - 1:name_range[1]]
        else:
            name_part = desired_name
        
        num_format = f"{i:0{num_digits}d}"
        
        new_filename = f"{name_part}_{num_format}.{target_extension}"
        
        source_path = os.path.join(directory, filename)
        
        target_path = os.path.join(directory, new_filename)
        
        os.rename(source_path, target_path)
        
        print(f"Переименован файл {filename} в {new_filename}")


directory = "C:\\Users\\zubko\OneDrive\\Рабочий стол\\test"
desired_name = "test2"
num_digits = 3  
source_extension = ".jpg" 
target_extension = "png" 
name_range = [3, 6]  

rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range)
