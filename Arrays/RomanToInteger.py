# https://leetcode.com/problems/roman-to-integer/

# using bruteforce

# def romanToInt(s):
#     result = 0
#     for i in range(len(s)):
#             match s[i]:
#                 case 'I': 
#                     if (i+1 <len(s)) and (s[i+1] in 'VX'):
#                         result -= 1
#                     else:
#                         result+=1
#                 case 'V':
#                      result += 5
#                 case 'X':
#                     if (i+1<len(s)) and (s[i+1] in 'LC'):
#                         result -= 10
#                     else:
#                         result += 10
#                 case 'L':
#                      result += 50
#                 case 'C':
#                     if (i+1<len(s)) and (s[i+1] in 'DM'):
#                         result -= 100
#                     else:
#                         result += 100
#                 case 'D':
#                      result += 500
#                 case 'M':
#                      result += 1000
#     return result


# using dictionary

def romanToInt(s):
    result = 0
    nums = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

    for i in range(len(s)):
            if i<len(s)-1 and nums[s[i]]<nums[s[i+1]]:
                result -= nums[s[i]]
            else:
                result+= nums[s[i]]
    return result

print(romanToInt('III'))