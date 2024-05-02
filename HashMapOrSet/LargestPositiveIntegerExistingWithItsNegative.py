# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

def findMaxK(nums):
    max_int = -1
    numset = set(nums)
    for num in nums:
        if num>max_int and -num in numset:
            max_int = num
    return max_int

print(findMaxK([-1,2,-3,3]))