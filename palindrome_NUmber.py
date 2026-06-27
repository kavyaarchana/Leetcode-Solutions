class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
            
        res *= sign
