class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
obj = Solution()
answer = obj.twoSum(nums, target)
print("Answer is:", answer)