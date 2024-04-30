# https://leetcode.com/problems/longest-common-prefix/

# METHOD 1 - BRUTEFORCE
# sort the array of strings
# loop 1: iterates through the first word and gets the current character
# loop 2: iterates through the list of strings starting from the second
#         compares the characters and returns the result if not matched

# METHOD 2 - Sort and compare first and last word
# sort the array of strings and get the first and the last word
# loop every character of the minimum length of both
# compare each, add to ans if match. return ans if not



def longestCommonPrefix(strs):
        # result = ""
        # strs.sort()
        # for i in range(len(strs[0])):
        #     ch = strs[0][i]
        #     for j in range(1,len(strs)):
        #           if strs[j][i] == ch:
        #                 continue
        #           else:
        #                 return result
        #     result += ch

        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans

print(longestCommonPrefix(["flower","flow","flight"]))