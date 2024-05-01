# https://leetcode.com/problems/unique-number-of-occurrences

def uniqueOccurrences(arr):
        dict = {}
        for i in arr:
            dict[i] = dict.get(i,0)+1
        num_of_occurance = []
        for value in dict.values():
            if value in num_of_occurance:
                return False
            num_of_occurance.append(value)
        return True

print(uniqueOccurrences([1,2,3,4,5]))