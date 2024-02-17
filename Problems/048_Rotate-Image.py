class Solution:
    
    # In-place
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def rotate(self, matrix):
        
        n = len(matrix)
        
        # Transposing matrix
        for i in range(0, n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reversing matrix
        for i in matrix:
            i.reverse()
        
        return matrix


    # Out-place
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    # def rotate(self, matrix):
    #     rotatedMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    #     print(rotatedMatrix)
        
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix)):
    #             print(rotatedMatrix)

    #             rotatedMatrix[j][len(matrix) - i - 1] = matrix[i][j]

    #     return rotatedMatrix


if __name__ == "__main__":
    test = Solution()
    print(test.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
