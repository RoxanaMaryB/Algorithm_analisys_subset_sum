import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def read_combined_csv(file_path):
    data = {
        'num_elements': [],
        'backtracking_memory': [],
        'dp_memory': [],
        'greedy_memory': []
    }
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data['num_elements'].append(int(row['num_elements']))
            data['backtracking_memory'].append(float(row['backtracking_memory']))
            data['dp_memory'].append(float(row['dp_memory']))
            data['greedy_memory'].append(float(row['greedy_memory']))
    return data

def average_duplicates(num_elements, memory):
    combined = defaultdict(list)
    for num, mem in zip(num_elements, memory):
        combined[num].append(mem)
    avg_num_elements = []
    avg_memory = []
    for num, mem_list in combined.items():
        avg_num_elements.append(num)
        avg_memory.append(np.mean(mem_list))
    return avg_num_elements, avg_memory

def plot_memory_vs_num_elements(data):
    plt.figure(figsize=(12, 8))

    algorithms = ['Backtracking', 'DP', 'Greedy']
    colors = ['blue', 'green', 'red']

    for algorithm, color in zip(algorithms, colors):
        memory = data[f'{algorithm.lower()}_memory']

        # Sort data by number of elements
        sorted_data = sorted(zip(data['num_elements'], memory))
        num_elements, memory = zip(*sorted_data)

        # Average duplicates
        num_elements, memory = average_duplicates(num_elements, memory)

        # Plot data points
        plt.scatter(num_elements, memory, label=f'{algorithm} Memory', s=50, color=color)

        # Polynomial regression for smooth curve
        poly_fit = np.polyfit(num_elements, memory, 3)
        poly_fit_fn = np.poly1d(poly_fit)
        num_elements_smooth = np.linspace(min(num_elements), max(num_elements), 300)
        memory_smooth = poly_fit_fn(num_elements_smooth)
        plt.plot(num_elements_smooth, memory_smooth, color=color, label=f'{algorithm} Fit')

    plt.xlabel('Number of Elements')
    plt.ylabel('Memory (MiB)')
    plt.yscale('log')  # Use logarithmic scale for better visualization
    plt.title('Number of Elements vs. Memory for Different Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig('combined_memory_vs_num_elements.png')
    plt.show()

if __name__ == "__main__":
    combined_csv_file = 'combined_results.csv'
    data = read_combined_csv(combined_csv_file)
    plot_memory_vs_num_elements(data)