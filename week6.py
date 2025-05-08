#problem 1
# def is_balanced(expression):
#     stack=[]
#
#     matching_bracket={
#         ')':'(',
#         '}':'{',
#         ']':'['
#     }
#     for char in expression:
#         if char in matching_bracket.values():
#             stack.append(char)
#         elif char in matching_bracket:
#             if stack and stack[-1] == matching_bracket[char]:
#                 stack.pop()
#             else:
#                 return False
#     return not stack
# print(is_balanced("{[()()]}"))
# print(is_balanced("{[(])}"))
#problem 2
# from inspect import stack
# def release_vehicles(entry_order,desired_order):
#     stack=[]
#     operations=[]
#     index=0
#     for vehicle in entry_order:
#         stack.append(vehicle)
#         operations.append(f"push{vehicle}")
#         while stack and stack[-1]==desired_order[index]:
#             stack.pop()
#             operations.append(f"pop()")
#             index+=1
#     if index==len(desired_order):
#         print("Valid sequence of operations:")
#         for op in operations:
#             print(op)
#     else:
#         print("Not possible to release in desired order.")
# entry_order=[2,1,3]
# desired_order=[1,2,3]
# release_vehicles(entry_order,desired_order)
#problem 4
import sys

def next_greater_element(arr):
    stack=[]
    nge=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            nge[i]=stack[-1]
        stack.append(arr[i])
    return nge
arr1=[3, 5, 2, 7]
arr2=[9,5,4,8]
print(next_greater_element(arr1))
print(next_greater_element(arr2))