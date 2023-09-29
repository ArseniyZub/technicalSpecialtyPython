import csv
import random

def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csvwriter.writerow(row)

generate_csv('file.csv', 100)