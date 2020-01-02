class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(x):
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
        count = 0
        for i in range(2, n):

            if isPrime(i):
                count += 1

        return count


s = Solution()
s.countPrimes(10)