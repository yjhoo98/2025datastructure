#problem 1
# def selectionSortAscending(L):
#     new_list=L.copy()
#     n=len(new_list)
#     new_list.sort()
#     return new_list
# def selectionSortDescending(L):
#     new_list=L.copy()
#     n=len(new_list)
#     new_list.sort(reverse=True)
#     return new_list
# lst=[65,85,55,93,35,95,87,78]
# print(f'Before:{lst}')
# print(f'Asc:{selectionSortAscending(lst)}/Dsc:{selectionSortDescending(lst)}')
#problem 2
# def selectionSort(L,key):
#     new_list=L.copy()
#     n=len(new_list)
#     for end in range(n-1,0,-1):
#         maxPos=0
#         for i in range(1,end+1):
#             if new_list[i][key]>new_list[maxPos][key]:
#                 maxPos=i
#         if maxPos!=end:
#             new_list[maxPos],new_list[end]=new_list[end],new_list[maxPos]
#
#     return new_list
# key=2
# students=[(202301,'alice',85),
#           (202102,'bob',95),
#           (202210,'charlie',78),
#           (202104,'david',92),
#           (202307,'eve',88)]
# print(f'before:{students}')
# print(f'asc:{selectionSort(students,key)}')
#problem 3
# def bubbleSort(L):
#     new_list=L.copy()
#     n=len(new_list)
#     pass_cnt=0
#     swap_cnt=0
#     compare_cnt=0
#     for end in range(n-1,0,-1):
#         pass_cnt+=1
#         for i in range(1,end+1):
#             compare_cnt+=1
#             if new_list[i-1]>new_list[i]:
#                 new_list[i],new_list[i-1]=new_list[i-1],new_list[i]
#                 swap_cnt+=1
#     return new_list,compare_cnt,pass_cnt,swap_cnt
# lst=[2,1,3,4,5,6,7,8,9,10]
# new_list,compare_cnt,pass_cnt,swap_cnt=bubbleSort(lst)
# print(f'before:{lst}')
# print(f'after:{new_list}')
# print(f'pass횟수:{pass_cnt}')
# print(f'swap횟수:{swap_cnt}')
# print(f'compare횟수:{compare_cnt}')
#problem4
# def insertionSort(L):
#     new_list=L.copy()
#     n=len(new_list)
#     for i in range(1,n):
#         x=new_list[i]
#         j=i-1
#         while j>=0:
#             if new_list[j]>x:
#                 new_list[j+1]=new_list[j]
#                 j-=1
#             else:
#                 break
#         new_list[j+1]=x
#     return new_list
# lst=[65,85,55,93,35,95,87,78]
# print(f'before:{lst}')
# print(f'after:{insertionSort(lst)}')
# sort(),sorted()
# name=['java','c','python','go']
# name.sort(key=len)
# print(f'{name}')
# def func(E):
#     return (-E[1],E[0])
# data=[('kim',5),('lee',4),('park',2),('hong',4),('cho',5)]
# print(sorted(data,key=func))
# print(sorted(data,key=lambda e:(-e[1],e[0
# ])))
#problem5
# def mergeSort(L):
#     if len(L)<=1:
#         return L.copy()
#     mid=len(L)//2
#     A=mergeSort(L[:mid])
#     B=mergeSort(L[mid:])
#     return merge(A,B)
# def merge(A,B):
#     result=[]
#     i=j=0
#     while i<len(A)and j<len(B):
#         if A[i]<B[j]:
#             result.append(A[i])
#             i+=1
#         else:
#             result.append(B[j])
#             j+=1
#     result.extend(A[i:])
#     result.extend(B[j:])
#
#     return result
# lst=[65,85,55,93,35,95,87,78]
# print(f'before:{lst}')
# print(f'after:{mergeSort(lst)}')
#problem 6
# def quickSort(L):
#     if len(L)<=1:
#         return L.copy()
#     pivot=L[-1]
#     left_list=[]
#     right_list=[]
#
#     for item in L[:-1]:
#         if item<pivot:
#             left_list.append(item)
#         else:
#             right_list.append(item)
#     return quickSort(left_list)+[pivot]+quickSort(right_list)
# lst=[65,85,55,93,35,95,87,78]
# print(f'before:{lst}')
# print(f'after:{quickSort(lst)}')
#problem7
n=int(input())
words=set()
for _ in range(n):
    word=input()
    words.add(word)
words=list(words)
words.sort(key=lambda x:(len(x),x))
for word in words:
    print(word)
