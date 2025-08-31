'''
One curious child has a set of N little bricks (5 ≤ N ≤ 500). From these bricks he builds different staircases. Staircase consists of steps of different sizes in a strictly descending order. It is not allowed for staircase to have steps equal sizes. Every staircase consists of at least two steps and each step contains at least one brick. Picture gives examples of staircase for N=11 and N=5:
Problem illustration
Your task is to write a program that reads the number N and writes the only number Q — amount of different staircases that can be built from exactly N bricks.
Input
Number N
Output
Number Q
Sample
inputoutput
212
995645335

'''

import sys
data=sys.stdin.read().strip().split()
if not data: sys.exit()
N=int(data[0])
dp=[0]*(N+1)
dp[0]=1
for x in range(1,N+1):
    for s in range(N,x-1,-1):
        dp[s]+=dp[s-x]
ans = dp[N]-1 if N>=1 else 0
if ans<0: ans=0
print(ans)