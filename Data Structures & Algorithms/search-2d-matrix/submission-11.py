class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l<=r:
            m = (r-l) //2 + l
            if matrix[m][-1] >= target and matrix[m][0] <= target:
                break
            elif matrix[m][-1] > target:
                r = m - 1
            else:
                l = m + 1
        ll, rr = 0, len(matrix[m]) - 1
        while ll<=rr:
            mm = (rr-ll) // 2 + ll
            if matrix[m][mm] == target:
                return True
            elif matrix[m][mm] > target:
                rr = mm - 1
            else:
                ll = mm + 1
        return False