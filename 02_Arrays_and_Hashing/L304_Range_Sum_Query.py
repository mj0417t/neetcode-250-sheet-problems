class NumMatrix:

    # def __init__(self, matrix: list[list[int]]):
    #     self.mat=list(matrix)
        

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sum=0
    #     for i in range(row1,row2+1):
    #         for j in range(col1, col2+1):
    #             sum+=self.mat[i][j]
    #     return sum


# #using 1D prefix sum
#     def __init__(self, matrix: list[list[int]]):
#         self.prefixSum=[[0]*len(matrix[0]) for _ in range(len(matrix))]
#         for row in range(len(matrix)):
#             self.prefixSum[row][0]=matrix[row][0]
#             for col in range(1, len(matrix[0])):
#                 self.prefixSum[row][col]=self.prefixSum[row][col-1]+matrix[row][col]


        

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         sum=0
#         for row in range(row1, row2+1):
#             if col1>0:
#                 sum+=self.prefixSum[row][col2]-self.prefixSum[row][col1-1]
#             else:
#                 sum+=self.prefixSum[row][col2]
#         return sum

#using 2D prefix sum
    def __init__(self, matrix: list[list[int]]):
        rows, cols=len(matrix),len(matrix[0])
        self.prefixSum=[[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            prefix=0
            for c in range(cols):
                prefix+=matrix[r][c]
                above=self.prefixSum[r][c+1]
                self.prefixSum[r+1][c+1]=prefix+above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight=self.prefixSum[row2+1][col2+1]
        above=self.prefixSum[row1][col2+1]
        left=self.prefixSum[row2+1][col1]
        topleft=self.prefixSum[row1][col1]
        return bottomRight-left-above+topleft
    

if __name__=='__main__':
    matrix=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj=NumMatrix(matrix)
    print(obj.sumRegion(2,1,4,3))
