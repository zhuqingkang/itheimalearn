class Solution:
    def countPrimes(self, n: int) -> int:
        data = [1]* n
        data[0], data[1] =0,0
        for i in range(2, n//2 + 1):
            if data[i] == 1:
                data[i * i:n:i] = [0] * len(data[i * i:n:i])
        return sum(data)
if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))