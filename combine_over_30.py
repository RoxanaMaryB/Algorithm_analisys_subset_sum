import os
import csv

def combine_csv_files(input_folders, output_file):
    combined_data = []
    fieldnames = ['num_elements', 'target', 'dp_time', 'dp_memory', 'greedy_time', 'greedy_memory']

    for folder in input_folders:
        csv_file_name = f'{folder}_metrics_results.csv'
        if os.path.exists(csv_file_name):
            with open(csv_file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    combined_data.append(row)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in combined_data:
            writer.writerow(row)

    print(f"Combined data saved to {output_file}")

if __name__ == "__main__":
    folders = ['subset_exists', 'subset_not_exists']
    output_file = 'combined_results2.csv'
    combine_csv_files(folders, output_file)