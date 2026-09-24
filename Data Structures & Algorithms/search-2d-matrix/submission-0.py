class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) -1
        while top <=bot: 
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid +1
            elif target < matrix[mid][0]:
                bot = mid -1
            else:
                row = matrix[mid]
                L = 0
                R = len(row) - 1
                
                while L <= R:
                    mid2 = (R+L)//2
                    if target > row[mid2]:
                        L = mid2 +1
                    elif target < row[mid2]:
                        R = mid2 -1
                    else:
                        return True
                return False
                
        return False

             

        