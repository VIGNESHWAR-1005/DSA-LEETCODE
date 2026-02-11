class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(1)   # last element is always 1
            
            # update from right to left
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row


        return row
        
        