# f(m, n) is the distinct number of paths
# base cases:
#   f(1,1)=1
#   f(1,2)=f(2,1)=1
#   f(2,2)=f(2,1)+f(1,2)=2
#   f(2,3)=f(2,2)+f(1,3)=2+1=3

#   f(2,4)=f(1,4)+f(2,3)=1+3=4
#   f(3,3)=f(3,2)+f(2,3)=6
#   f(3,4)=f(2,4)+f(3,3)=4+6=10

#   f(m,n)=f(m-1,n)+f(m,n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                if i==0:
                    dp[i].append(1)
                elif j==0:
                    dp[i].append(1)
                
                else:
                    dp[i].append(dp[i][j-1]+dp[i-1][j])
        return dp[m-1][n-1]