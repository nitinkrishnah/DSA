# https://leetcode.com/problems/find-the-difference-of-two-arrays


def findDifference(nums1, nums2):
        first = list(set(nums1) - set(nums2))
        second = list(set(nums2) - set(nums1))
        return [first, second]

print(findDifference([1,2,3,4],[3,4,5,6]))