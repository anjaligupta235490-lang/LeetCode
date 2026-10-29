class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        even = (n+1)//2
        odd = n//2
        MOD = (10**9) + 7
        def pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result *base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
        a = pow(5, even)
        b = pow(4, odd)
        result = (a * b) % MOD
        return result            

         
