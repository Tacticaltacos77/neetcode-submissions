class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        out = False
        l, r = 0, m*n-1
        
        while l <= r:
            mid = (r-l)//2 +l
            midN = mid//n
            midM = mid%n
            if target > matrix[midN][midM]:
                l = mid+1
            elif target < matrix[midN][midM]:
                r = mid-1
            else:
                out =True
                break
        return out
