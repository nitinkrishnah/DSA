# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# LOGIC
# The first element i.e element at index 0 is always least and it should be in final nums
# So we have to make changes from the second element onwards so j=1
# We find a new number when previous number is not equal tp current number, SO we update nums and increment j


def removeDuplicates( nums) :
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j

print(removeDuplicates([0,0,0,1,1,2,3,4,4,5,5,5,5,6]))
