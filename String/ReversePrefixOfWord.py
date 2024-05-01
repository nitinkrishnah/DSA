# https://leetcode.com/problems/reverse-prefix-of-word/description/


def reversePrefix(word, ch):
    idx = word.find(ch)
    prefix = word[:idx+1]
    ans = prefix[::-1]
    ans = ans + word[idx+1:]
    return ans

print(reversePrefix('abcdefd','d'))