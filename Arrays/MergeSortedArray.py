def merge(nums1, m, nums2, n):
        if n == 0:
            return nums1
        i , j = 0,0

        while i<m+n and j<n:
            val1,val2 = nums1[i],nums2[j]
            if val1>val2:
                nums1.insert(i,nums2[j])
                j+=1
            i+=1 

        i = i-(n-j)
        
        while j<n:
             nums1.insert(i,nums2[j])
             j+=1
             i+=1
        while len(nums1)>m+n:
            nums1.pop()
        return nums1

        # j = 0
        # for i in range(m, m + n):
        #     nums1[i] = nums2[j]
        #     j += 1

        # nums1.sort()

print(merge([1,2,3,0,0,0],3,[4,5,6],3))