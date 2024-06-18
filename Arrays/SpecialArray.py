# Special Array With X Elements Greater Than or Equal X

# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

def specialArray(nums):
        nums.sort()
        n = len(nums)
    
        for x in range(1, n + 1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            if count == x:
                return x
        return -1