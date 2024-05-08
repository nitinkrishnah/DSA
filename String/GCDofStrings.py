# https://leetcode.com/problems/greatest-common-divisor-of-strings

def gcdOfStrings(str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return gcdOfStrings(str1[len(str2):], str2)
        return gcdOfStrings(str1, str2[len(str1):])

print(gcdOfStrings("ABABAB","AB"))