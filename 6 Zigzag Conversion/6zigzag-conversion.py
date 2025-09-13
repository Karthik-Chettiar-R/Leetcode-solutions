class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s

        zigzag = [[""] * len(s) for _ in range(numRows)]
        curRow, curCol = 0, 0
        goingDown = True

        for ch in s:
            zigzag[curRow][curCol] = ch
            if goingDown:
                if curRow == numRows - 1:
                    goingDown = False
                    curRow -= 1
                    curCol += 1
                else:
                    curRow += 1
            else:
                if curRow == 0:
                    goingDown = True
                    curRow += 1
                else:
                    curRow -= 1
                    curCol += 1

        
        result = ""
        for row in zigzag:
            result += "".join(row)
        return result