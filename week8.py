#problem1 factorial
# def fac(n):
#     if n==1 or n==0:
#         return 1
#
#     else:
#         return n*fac(n-1)
# print(fac(0))
# print(fac(1))
# print(fac(3))
# print(fac(5))
#problem2 GCD
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(82,123))
#problem3 series
# def S(n):
#     if n==1:
#         return 1.0
#     if n%2==0:
#         return S(n-1)-1/n
#     else:
#         return S(n-1)+1/n
# print(S(2))
#problem4 Exponentiation
# import time
# def power1(x,n):
#     if n==1:
#         return x
#     return power1(x,n-1)*x
# def power2(x,n):
#     if n==1:
#         return x
#     y=power2(x,n//2)
#     if n%2==0:
#         return y*y
#     else:
#         return y*y*x
# start1=time.time()
# print(power1(3,5))
# end1=time.time()
# print(end1-start1)
# start2=time.time()
# print(power2(3,5))
# end2=time.time()
# print(end2-start2)
#problem5
# def isPalindrome(str):
#     if len(str)<=1:
#         return True
#     if str[0]==str[-1]:
#         return isPalindrome(str[1:-1])
#     else:
#         return False
# print(isPalindrome('banana'))
#problem6
def count(n, max):
    if n==0:
        return 1
    if max==0 or n<0:
        return 0
    return count(n - max, max)+count(n, max - 1)
def tower(n):
    return count(n,n)
print(tower(5))
