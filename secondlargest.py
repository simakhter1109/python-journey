def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 5, 30, 30]))