# https://leetcode.com/problems/relative-ranks/

def findRelativeRanks(score):
        N = len(score)
       
        # Save the index of each athelete
        score_to_index = {}
        for i in range(N):
            score_to_index[score[i]] = i

        # Sort score in descending order
        score.sort(reverse = True)

        # Assign ranks to athletes
        rank = [" "] * N
        for i in range(N):
            if i == 0:
                rank[score_to_index[score[i]]] = "Gold Medal"
            elif i == 1:
                rank[score_to_index[score[i]]] = "Silver Medal"
            elif i == 2:
                rank[score_to_index[score[i]]] = "Bronze Medal"
            else:
                rank[score_to_index[score[i]]] = str(i + 1)

        return rank

print(findRelativeRanks([1,2,3,4]))