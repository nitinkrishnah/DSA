# https://leetcode.com/problems/maximize-happiness-of-selected-children/

#BRUTEFORCE - Almost all test cases passed
#PROBLEM : We are iterating over entire array everytime
# def maximumHappinessSum( happiness, k):
#         happiness.sort(reverse = True)
#         maxHappy = 0
#         idx = 0
#         while k!=0:
#             if happiness[idx]>0:
#                 maxHappy += happiness[idx]
#                 idx+=1
#                 for i in range(idx,len(happiness)):
#                     happiness[i] = happiness[i]-1 if happiness[i]>0 else happiness[i]    
#                 k-=1
#             else:
#                 break
#         return maxHappy

#GREEDY
# 1. We sort the given array in descending order
# 2. initialize an i(index) which serves both as a deductor and highest item index
# 3. Iterate untill k is positive
# 4. Get the maximum of that iteration by getting the happiness[i](ith element) and subtract 
# it by the number of times of itertion
# 5. Update the result and also the k value
def maximumHappinessSum( happiness, k):
    happiness.sort(reverse=True)
    i = 0
    res = 0

    while k > 0:
            val = happiness[i] - i
            if val>0:
                res += val
                i += 1
                k -= 1
            else:
                break

    return res


print(maximumHappinessSum([1,2,3],2))