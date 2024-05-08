# https://leetcode.com/problems/ransom-note/

def canConstruct(ransomNote, magazine):
        chars = {}
        for char in magazine:
            chars[char] = chars.get(char,0) + 1

        for ch in ransomNote:
            if ch in chars and chars[ch]>0:
                chars[ch]-= 1
            else:
                return False
        return True

        # st1, st2 = Counter(ransomNote), Counter(magazine)
        # if st1 & st2 == st1:
        #     return True
        # return False

print(canConstruct("Nitin","Nitin Krishna"))