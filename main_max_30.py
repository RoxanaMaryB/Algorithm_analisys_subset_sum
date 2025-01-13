import os
import csv
from measure import measure_time_and_memory
from backtracking import subset_sum_backtracking
from dp import subset_sum_dp
from greedy import subset_sum_greedy

def read_test_cases(folder_path):
    test_cases = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder_path, file_name), 'r') as f:
                lines = f.readlines()
                N, T = map(int, lines[0].strip().split())
                values = [int(line.strip()) for line in lines[1:N+1]]
                test_cases.append((values, T))
    return test_cases

def process_folder(folder_name):
    # Variables to accumulate total times and memory usage
    backtracking_time_total = 0
    dp_time_total = 0
    greedy_time_total = 0
    backtracking_memory_total = 0
    dp_memory_total = 0
    greedy_memory_total = 0

    # Variables to count successful and unsuccessful attempts
    backtracking_found = 0
    backtracking_not_found = 0
    dp_found = 0
    dp_not_found = 0
    greedy_found = 0
    greedy_not_found = 0

    # Read test cases from folder
    test_cases = read_test_cases(folder_name)

    # Lists to store results
    metrics_results = []
    outputs_results = []

    # Test each algorithm with the generated test cases
    for i, (arr, target) in enumerate(test_cases):
        try:
            print(f"Processing test case {i+1}/{len(test_cases)}: {arr} with target {target}")

            # Test backtracking
            subset_backtracking, backtracking_time, backtracking_memory = measure_time_and_memory(subset_sum_backtracking, arr, target)
            backtracking_time_total += backtracking_time
            backtracking_memory_total += backtracking_memory
            if subset_backtracking:
                backtracking_found += 1
            else:
                backtracking_not_found += 1
            print(f"Backtracking completed for test case {i+1}/{len(test_cases)}")

            # Test dynamic programming
            subset_dp, dp_time, dp_memory = measure_time_and_memory(subset_sum_dp, arr, target)
            dp_time_total += dp_time
            dp_memory_total += dp_memory
            if subset_dp:
                dp_found += 1
            else:
                dp_not_found += 1
            print(f"DP completed for test case {i+1}/{len(test_cases)}")

            # Test greedy
            subset_greedy, greedy_time, greedy_memory = measure_time_and_memory(subset_sum_greedy, arr, target)
            greedy_time_total += greedy_time
            greedy_memory_total += greedy_memory
            if subset_greedy:
                greedy_found += 1
            else:
                greedy_not_found += 1
            print(f"Greedy completed for test case {i+1}/{len(test_cases)}")

            # Check for discrepancies in outputs
            if subset_backtracking != subset_dp or subset_backtracking != subset_greedy or subset_dp != subset_greedy:
                print(f"Discrepancy found for test case {arr} with target {target}:")
                print(f"Backtracking output: {subset_backtracking}")
                print(f"DP output: {subset_dp}")
                print(f"Greedy output: {subset_greedy}")

            # Append results for this test case
            metrics_results.append({
                'num_elements': len(arr),
                'target': target,
                'backtracking_time': backtracking_time,
                'backtracking_memory': backtracking_memory,
                'dp_time': dp_time,
                'dp_memory': dp_memory,
                'greedy_time': greedy_time,
                'greedy_memory': greedy_memory
            })

            outputs_results.append({
                'num_elements': len(arr),
                'target': target,
                'backtracking_output': subset_backtracking,
                'dp_output': subset_dp,
                'greedy_output': subset_greedy
            })
        except Exception as e:
            print(f"Error processing test case {arr} with target {target}: {e}")

    # Save metrics results to CSV file
    metrics_csv_file_name = f'{folder_name}_metrics_results.csv'
    with open(metrics_csv_file_name, 'w', newline='') as csvfile:
        fieldnames = ['num_elements', 'target', 'backtracking_time', 'backtracking_memory', 'dp_time', 'dp_memory', 'greedy_time', 'greedy_memory']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in metrics_results:
            writer.writerow(result)

    print(f"Metrics results saved to {metrics_csv_file_name}")

    # Save outputs results to CSV file
    outputs_csv_file_name = f'{folder_name}_outputs_results.csv'
    with open(outputs_csv_file_name, 'w', newline='') as csvfile:
        fieldnames = ['num_elements', 'target', 'backtracking_output', 'dp_output', 'greedy_output']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in outputs_results:
            writer.writerow(result)

    print(f"Outputs results saved to {outputs_csv_file_name}")

if __name__ == "__main__":
    folders = ['subset_exists', 'subset_not_exists']  # Process all folders
    for folder in folders:
        process_folder(folder)