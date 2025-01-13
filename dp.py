def subset_sum_dp(nums, target):
    if target == 0:
        return True
    if not nums:
        return False

    set_sum = sum(nums)
    if target > set_sum:
        return False

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                if dp[target]:
                    return True

    return dp[target]