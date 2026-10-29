class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        MOD = (10**9) + 7
        def pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result *base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
       
        return   pow(5, (n+1)//2) * pow(4, n//2) % MOD       

         
