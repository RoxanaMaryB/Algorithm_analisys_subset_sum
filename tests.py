import os
import random

def save_test_cases(test_cases, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for i, (N, T, values) in enumerate(test_cases):
        with open(os.path.join(folder_name, f'test{i+1:02d}.txt'), 'w') as f:
            f.write(f"{N} {T}\n")
            for value in values:
                f.write(f"{value}\n")

def generate_test_cases():
    # Tests where a subset with the target sum exists
    exists_tests = [
        (3, 6, [1, 2, 3]),  # 1+2+3 = 6
        (4, 10, [1, 2, 3, 4]),  # 1+2+3+4 = 10
        (4, 10, [2, 3, 5, 7]),  # 3+7 = 10
        (5, 15, [5, 5, 5, 5, 5]),  # 5+5+5 = 15
        (6, 21, [1, 2, 3, 4, 5, 6]),  # 1+2+3+4+5+6 = 21
    ]
    # Generate additional test cases where a subset exists
    for N in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
        values = [random.randint(1, 500) for _ in range(N)]
        subset = random.sample(values, N // 5)
        T = sum(subset)
        if T <= 10**6:
            exists_tests.append((N, T, values))
    save_test_cases(exists_tests, 'subset_exists')

    # Tests where a subset with the target sum does not exist
    not_exists_tests = [
        (3, 7, [1, 2, 3]),
        (4, 11, [1, 2, 3, 4]),
        (4, 11, [2, 3, 5, 7]),
        (5, 16, [5, 5, 5, 5, 5]),
        (6, 22, [1, 2, 3, 4, 5, 6]),
    ]
    # Generate additional test cases where no subset exists
    for N in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
        values = [random.randint(1, 500) for _ in range(N)]
        T = sum(values) + 1  # Set target to a value larger than the sum of all elements
        if T <= 10**6:
            not_exists_tests.append((N, T, values))
    save_test_cases(not_exists_tests, 'subset_not_exists')

if __name__ == "__main__":
    generate_test_cases()