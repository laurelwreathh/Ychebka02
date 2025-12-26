def solve(nums, prev=-999999999):
    if not nums:
        return []

    first = nums[0]

    if first > prev:
        take = [first] + solve(nums[1:], first)
        skip = solve(nums[1:], prev)
        return take if len(take) > len(skip) else skip
    else:
        return solve(nums[1:], prev)


print(solve([6, 2, 5, 4, 2, 5, 6]))
print(solve([7, 3, 8, 4, 2, 5, 6]))
