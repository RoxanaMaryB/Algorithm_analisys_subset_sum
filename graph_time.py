import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from collections import defaultdict

def read_combined_csv(file_path):
    data = {
        'num_elements': [],
        'backtracking_time': [],
        'dp_time': [],
        'greedy_time': []
    }
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data['num_elements'].append(int(row['num_elements']))
            data['backtracking_time'].append(float(row['backtracking_time']))
            data['dp_time'].append(float(row['dp_time']))
            data['greedy_time'].append(float(row['greedy_time']))
    return data

def average_duplicates(num_elements, times):
    combined = defaultdict(list)
    for num, time in zip(num_elements, times):
        combined[num].append(time)
    avg_num_elements = []
    avg_times = []
    for num, time_list in combined.items():
        avg_num_elements.append(num)
        avg_times.append(np.mean(time_list))
    return avg_num_elements, avg_times

def plot_time_vs_num_elements(data):
    plt.figure(figsize=(12, 8))

    algorithms = ['Backtracking', 'DP', 'Greedy']
    colors = ['blue', 'green', 'red']

    for algorithm, color in zip(algorithms, colors):
        times = data[f'{algorithm.lower()}_time']

        sorted_data = sorted(zip(data['num_elements'], times))
        num_elements, times = zip(*sorted_data)

        num_elements, times = average_duplicates(num_elements, times)

        plt.scatter(num_elements, times, label=f'{algorithm} Time', s=50, color=color)

        if algorithm == 'Backtracking':
            log_times = np.log(times)
            num_elements_smooth = np.linspace(min(num_elements), max(num_elements), 300)
            spline = make_interp_spline(num_elements, log_times, k=3)
            log_times_smooth = spline(num_elements_smooth)
            times_smooth = np.exp(log_times_smooth)
            plt.plot(num_elements_smooth, times_smooth, color=color, label=f'{algorithm} Fit')
        else:
            poly_fit = np.polyfit(num_elements, times, 3)
            poly_fit_fn = np.poly1d(poly_fit)
            num_elements_smooth = np.linspace(min(num_elements), max(num_elements), 300)
            times_smooth = poly_fit_fn(num_elements_smooth)
            plt.plot(num_elements_smooth, times_smooth, color=color, label=f'{algorithm} Fit')

    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.yscale('log')
    plt.title('Number of Elements vs. Time for Different Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig('combined_time_vs_num_elements.png')
    plt.show()

if __name__ == "__main__":
    combined_csv_file = 'combined_results.csv'
    data = read_combined_csv(combined_csv_file)
    plot_time_vs_num_elements(data)