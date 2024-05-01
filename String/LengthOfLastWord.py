# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s):
    return len(s.split()[-1])


print(lengthOfLastWord('   fly me   to   the moon  '))