def subset_sum_greedy(numbers, target):
    numbers = sorted(numbers, reverse = True)
    current_sum = 0

    for num in numbers:
        if current_sum + num <= target:
            current_sum += num

        if current_sum == target:
            return True

    return False