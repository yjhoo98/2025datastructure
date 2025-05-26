#problem 1
# def sequential_search(students,target_id):
#     for i in range(len(students)):
#         if target_id==students[i][0]:
#             return i
#     return len(students)
# students=[(11,'ryu',95),(12,'park',97),(15,'kim',89)]
# print(sequential_search(students,15))
# print(sequential_search(students,5))
#problem 2
#using while loop
# def bin_search(L,id):
#     low,high=0,len(L)-1
#
#     while low<=high:
#         mid=(low+high)//2
#         if id==L[mid][0]: return mid
#         elif id<L[mid][0]: high=mid-1
#         else:low=mid+1
#     return len(L)
# students=[(11,'ryu',95),(12,'park',97),(15,'kim',89)]
# print(sequential_search(students,15))
# print(sequential_search(students,5))
#using recursion
# def bin_search2(L,low,high,id):
#     if low>high:
#         return len(L)
#     mid=(low+high)//2
#     if id==L[mid][0]:
#         return mid
#     if id<L[mid][0]:
#         return bin_search2(L,low,mid-1,id)
#     else:
#         return bin_search2(L,mid+1,high,id)
# students=[(11,'ryu',95),(12,'park',97),(15,'kim',89)]
# print(sequential_search(students,15))
# print(sequential_search(students,5))
#problem 5
# def upperBound(L,value):
#     low,high=0,len(L)-1
#     while low<=high:
#         mid=(low+high)//2
#         if value<L(mid):high=mid-1
#         else:low=mid+1
#     return high+1
# L=[10,20,30,40,50]
# print(f'upper bound:{upperBound(L,20)}')
# print(f'No such upper bound exists:{upperBound(L,100)}')
#problem 6
# def lowerBound(L,value):
#     low,high=0,len(L)-1
#
#     while low<=high:
#         mid=(low+high)//2
#         if value<=L[mid]:high=mid-1
#         else:low=mid+1
#     return high+1
# L=[10,20,30,40,50]
# print(f'lower bound:{lowerBound(L,20)}')
# print(f'No such lower bound exists:{lowerBound(L,100)}')
#problem 7
# import sys
# from io import StringIO
# input_data="""5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# """
# sys.stdin=StringIO(input_data)
# N=int(input())
# A=set(map(int,input().split()))
# M=int(input())
# queries=list(map(int,input().split()))
# for x in queries:
#     if x in A:
#         print(1)
#     else:
#         print(0)
#problem 8
# from collections import  Counter
# N=int(input())
# cards=list(map(int,input().split()))
# M=int(input())
# queries=list(map(int,input().split()))
# card_counts=Counter(cards)
# result=[str(card_counts[q]) for q in queries]
# print(''.join(result))