# https://leetcode.com/problems/palindrome-number/


def isPalindrome( x):
        if x<0:
            return False
        reversed = 0
        temp = x
        while temp!=0:
            digit = temp % 10
            reversed = reversed * 10 + digit
            temp = temp // 10
        return x == reversed

print(isPalindrome(121))