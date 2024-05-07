# https://leetcode.com/problems/make-a-square-with-the-same-color/

def canMakeSquare(grid):
        def change(x, y):
            colors = [grid[x][y], grid[x][y+1], grid[x+1][y], grid[x+1][y+1]]
            count = {'B': 0, 'W': 0}
            for c in colors:
                count[c] += 1
            return count['B'] >= 3 or count['W'] >= 3

        for i in range(2):
            for j in range(2):
                if change(i, j):
                    return True
        return False

print(canMakeSquare([["B","W","B"],["B","W","W"],["B","W","B"]]))