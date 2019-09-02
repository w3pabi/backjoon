import sys


a = sys.stdin.readline().strip().upper()
b = sys.stdin.readline().strip().upper()
alen = len(a) + 1
blen = len(b) + 1
dp = [[0] * alen for _ in range(blen)]

for i in range(1, blen):
    for j in range(1, alen):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1] + (a[i-1] == b[j-1]))

print(dp[alen-1][blen-1])