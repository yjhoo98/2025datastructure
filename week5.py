#immutable
# a=10
# b=10
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a=11
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
#mutable
# a=[10]
# b=[10]
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a.append(99)
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a=[10]
# b=a
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a.append(99)
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
#deep copy using copy()
import copy

# a=[10]
# b=a.copy()
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a.append(99)
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
#deep copy using slicing
# a=[10]
# b=a[:]
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a.append(99)
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
#deep copy using deepcopy()
# a=[10]
# b=copy.deepcopy(a)
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
# a.append(99)
# print(f'a의 원소:{a}, b의 원소:{b}')
# print(f'a의 주솟값:{id(a)},b의 주솟값:{id(b)}')
#problem1
# list1=[[0 for _ in range(4)] for _ in range(3)]
# print(list1)
#problem2
# n=int(input())
# for i in range(n):
#     s=input()
#     score=0
#     add=0
#     temp=[]
#     for j in range(len(s)):
#         if s[j]=='O':
#             add+=1
#             temp.append(add)
#         elif s[j]=='X':
#             add=0
#     for k in range(len(temp)):
#         score+=temp[k]
#     print(score)
#problem3
import sys
N,M=map(int, sys.stdin.readline().split())
arr=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K=int(sys.stdin.readline())
do=[list(map(int, sys.stdin.readline().split())) for _ in range(K)]

dp=[[0 for i in range(M+1)] for _ in range(N+1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]+arr[i-1][j-1]-dp[i-1][j-1]
for _, line in enumerate(do):
    i,j,x,y=line
    print(dp[x][y]-(dp[x][j-1]+dp[i-1][y])+dp[i-1][j-1])