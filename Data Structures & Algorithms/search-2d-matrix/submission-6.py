class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        q, m = 0, len(matrix)-1
        m_index = 0

        while q <= m:
            x = q + ((m - q)//2)

            if x < len(matrix) - 1 and matrix[x][0] <= target < matrix[x+1][0]:
                l, r = 0, len(matrix[x])-1

                while l <= r:
                    p = l + ((r - l)//2)

                    if target < matrix[x][p]:
                        r = p - 1

                    elif target > matrix[x][p]:
                        l = p + 1

                    else:
                        return True

                return False

            elif matrix[x][0] <= target and x == len(matrix)-1:
                l, r = 0, len(matrix[x])-1

                while l <= r:
                    p = l + ((r - l)//2)

                    if target < matrix[x][p]:
                        r = p - 1

                    elif target > matrix[x][p]:
                        l = p + 1

                    else:
                        return True

                return False
            
            elif target < matrix[x][0]:
                m = x - 1

            else:
                q = x + 1

        return False