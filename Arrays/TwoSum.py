# https://leetcode.com/problems/two-sum/

# one pass hash method O(n) time and o(n) space
# using dictionary(most efficient)
# declare an empty dictionary
# loop through the array
#     for every number in array
#         calculate the difference
#         check if difference is already in dictionary
#             if yes return the indices
#             else add the number as key and index as Value


def twoSum(nums, target):
        nmap = {}
        for i in range(len(nums)):
            num=nums[i]
            diff = target - num
            if diff in nmap:
                return [i,nmap[diff]]
            nmap[num]=i
        return []

result = twoSum([3,2,4],6)
print(result)