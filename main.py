import csv
import sys

# Increase the field size limit
csv.field_size_limit(sys.maxsize)

csv_file_path = 'path_to_your_csv_file.csv'

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader) - 1  # Subtract 1 to exclude the header row

print(f'Total number of samples: {row_count}')
