# https://leetcode.com/problems/valid-palindrome/

#Using bruteforce
# def isPalindrome(s):
#         left = 0
#         right = len(s)-1
#         while left<right:
#             if not s[left].isalnum():
#                 left+=1
#             elif not s[right].isalnum():
#                 right-=1
#             elif s[left].lower() == s[right].lower():
#                 left+=1
#                 right-=1
#             else:
#                 return False
#         return True

def isPalindrome(s):
        newstr=""
        for c in s:
            if c.isalnum():
                newstr+=c.lower()
        return newstr==newstr[::-1]



print(isPalindrome("Nitin"))