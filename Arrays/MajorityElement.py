# https://leetcode.com/problems/majority-element/

def majorityElement(nums):
        # majority = len(nums)/2
        # dictionary = {}
        # for i in nums:
        #     dictionary[i] = dictionary.get(i,0)+1
        # for key,value in dictionary.items():
        #     if value> majority:
        #         return key

        nums.sort()
        return nums[len(nums)//2]

print(majorityElement([1,2,3,3]))