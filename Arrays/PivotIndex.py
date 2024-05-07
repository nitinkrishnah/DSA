def pivotIndex(nums):
        # create two arrays for leftsum and right sum
        sumLeft = [0 for i in nums]
        sumRight = [0 for i in nums]
        
        for i in range(len(nums)-1):
            sumLeft[i+1] = sumLeft[i] + nums[i]

        for i in range(len(nums)-1,0,-1):
            sumRight[i-1] = sumRight[i] + nums[i]

        # iterate through two arrays and return index value when both are equal
        for i in range(len(nums)):
            if sumLeft[i] == sumRight[i]:
                return i

        return -1

print(pivotIndex([1,7,3,6,5,6]))