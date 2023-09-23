import os
import json
import csv
import pickle

def calculate_directory_size(directory_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def directory_to_dict(directory_path):
    dir_info = {"type": "directory", "size": calculate_directory_size(directory_path)}
    dir_info["content"] = []

    for dirpath, dirnames, filenames in os.walk(directory_path):
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            dir_info["content"].append(directory_to_dict(subdir_path))
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_info = {"type": "file", "size": os.path.getsize(filepath)}
            dir_info["content"].append(file_info)

    return dir_info

def save_to_json_csv_pickle(data, directory_path):
    json_path = os.path.join(directory_path, "directory_structure.json")
    csv_path = os.path.join(directory_path, "directory_structure.csv")
    pickle_path = os.path.join(directory_path, "directory_structure.pkl")

    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    with open(csv_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["type", "size"])
        write_csv_data(data, csv_writer)

    with open(pickle_path, "wb") as pickle_file:
        pickle.dump(data, pickle_file)

def write_csv_data(data, csv_writer):
    for item in data["content"]:
        csv_writer.writerow([item["type"], item["size"]])
        if item["type"] == "directory":
            write_csv_data(item, csv_writer)


directory_path = "C:\\Users\\zubko\\OneDrive"
directory_data = directory_to_dict(directory_path)
save_to_json_csv_pickle(directory_data, directory_path)
