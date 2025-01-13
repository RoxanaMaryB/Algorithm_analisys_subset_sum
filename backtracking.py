def backtracking(S, index, target):
    if index >= len(S):
        return target == 0
    if target < 0:
        return False
    # Try including the current element
    include = backtracking(S, index + 1, target - S[index])
    # Try excluding the current element
    exclude = backtracking(S, index + 1, target)
    return include or exclude

def subset_sum_backtracking(nums, target):
    nums.sort()
    return backtracking(nums, 0, target)