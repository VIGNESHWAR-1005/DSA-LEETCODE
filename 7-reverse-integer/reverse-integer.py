
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        
        while x != 0:
            digit = int(x % 10)
            
            # Handle negative numbers correctly in Python
            if x < 0 and digit > 0:
                digit -= 10
            
            # Overflow check BEFORE updating result
            if result > 214748364 or (result == 214748364 and digit > 7):
                return 0
            if result < -214748364 or (result == -214748364 and digit < -8):
                return 0
            
            result = result * 10 + digit
            x = int(x / 10)  # important: truncate toward zero
        
        return result