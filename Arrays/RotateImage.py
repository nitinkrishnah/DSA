# https://leetcode.com/problems/rotate-image/description/

def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
            row.reverse()
        print(matrix)

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))