from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            col_index = matrix[i].index(row_min)
            
            is_max = True
            for k in range(len(matrix)):
                if matrix[k][col_index] > row_min:
                    is_max = False
                    break
            
            if is_max:
                result.append(row_min)
        
        return result