#problem 1
# def isExist(x):
#     list1=[5,10,15,20,25]
#     if x in list1:
#         return True
#     else:
#         return False
# num=int(input("number:"))
#
# if isExist(num):
#     print(f'{num} exists in list')
# else:
#     print(f'{num} does not exist in list')
#problem 2
# import time
# start=time.time()
# for i in range(0,10000000):
#     pass
# stop=time.time()
# print(f'{round(stop-start,3)}')
#problem 3
# def a(n):
#     count=0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 count+=1
#     print(f'{count}')
#time complexity:O(n^3)
#problem 4
# def b(n):
#     count=0
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             count+=1
#     print(f'{count}')
#time complexity:n(n+1)/2->O(n^2)
#problem 5
# def c(n):
#     count=0
#     for i in range(n):
#         j=n
#         while j>=1:
#             count+=1
#             j//2
#     return count
#time complexity:O(nlogn)
#problem 6
# def program_D(n) :
#     count = 0
#     for i in range(1, n+1) :
#         for j in range(1, n//i + 1) :
#             count += 1
#     return count
#time complexity:O(nlogn)
#problem 7:O(n^2)
#problem 8:Number of operations performed
#problem 9:doubles
#problem 10:T2=T1x(n2/n1)^3->T2=1x(10)^3=16.40m
#problem 11:O(1)>O(logn)>O(n)>O(nlogn)>O(n^2)>O(2^n)>O(n!)
#problem 12: 1)no 2)about n=20