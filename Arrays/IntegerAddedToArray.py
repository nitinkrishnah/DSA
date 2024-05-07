# https://leetcode.com/problems/find-the-integer-added-to-array-i/

def addedInteger(num1, num2):
    if len(num1) == 1:
        return num2[0] - num1[0]
    least_num1,least_num2 = num1[0],num2[0]
    for i in range(len(num1)):
        if num1[i]<least_num1:
            least_num1 = num1[i]
        if num2[i]<least_num2:
           least_num2 = num2[i] 
    return least_num2 - least_num1  

print(addedInteger([2,6,4],[9,7,5]))