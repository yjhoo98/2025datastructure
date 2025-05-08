#problem 1
from queue import Queue
from collections import deque
# list
# class ListQueue():
#     def __init__(self):
#         self.list=[]
#
#     def empty(self):
#         return len(self.list)==0
#
#     def enqueue(self,item):
#         self.list.append(item)
#
#     def enqueue_front(self,item):
#         self.list.insert(0,item)
#
#     def front(self):
#         if self.empty():
#             return None
#         return self.list[0]
#
#     def dequeue(self):
#         if self.empty()
#             return None
#         return self.list.pop(0)
#
#     def dequeue_back(self):
#         if self.empty():
#             return None
#         return self.list.pop()
#queue.Queue
# class QueueQueue():
#     def __init__(self):
#         self.queue=Queue()
#     def empty(self):
#         return self.queue.empty()
#     def enqueue(self,item):
#         self.queue.put(item)
#     def front(self):
#         if self.empty():
#             return None
#         return self.queue.queue[0]
#     def dequeue(self):
#         if self.empty():
#             return None
#         return self.queue.get()
#deque
# class DequeQueue():
#     def __init__(self):
#         self.queue=deque()
#     def empty(self):
#         return len(self.queue)==0
#     def enqueue(self,item):
#         self.queue.append(item)
#     def enqueue_front(self,item):
#         self.queue.appendleft(item)
#     def front(self):
#         if self.empty():
#             return None
#         return self.queue[0]
#     def back(self):
#         if self.empty():
#             return None
#         return self.queue[-1]
#     def dequeue(self):
#         if self.empty():
#             return None
#         return self.queue.popleft()
#     def dequeue_back(self):
#         if self.empty():
#             return None
#         return self.queue.pop()
# print("[리스트 기반 큐]")
# lq=ListQueue()
# lq.enqueue(1)
# lq.enqueue(2)
# lq.enqueue_front(0)
# print("현재 상태:",lq.list)
# print("앞쪽 삭제:",lq.dequeue())
# print("뒤쪽 삭제:",lq.dequeue_back())
# print("현재 상태:",lq.list)
# print("[queue.Queue 기반 큐]")
# qq=QueueQueue()
# qq.enqueue(1)
# qq.enqueue(2)
#
# print("현재 상태:",list(qq.queue.queue))
# print("삭제:",qq.dequeue())
# print("현재 상태:",list(qq.queue.queue))
# print("[deque 기반 큐]")
# dq=DequeQueue()
# dq.enqueue(1)
# dq.enqueue(2)
# dq.enqueue_front(0)
# print("현재 상태:",list(dq.queue))
# print("앞쪽 삭제:",qq.dequeue())
# print("뒤쪽 삭제:",dq.dequeue_back())
# print("현재 상태:",list(dq.queue))
#problem2 Josephus Problem
#using deque
# def josephus_deque(n,k):
#     queue=deque(range(1,n+1))
#     result=[]
#
#     while queue:
#         queue.rotate(-(k-1))
#         result.append(str(queue.popleft()))
#     return "<"+",".join(result)+">"
# n,k=map(int,input('Write n and k separated by a space: ').split())
# print(josephus_deque(n,k))
#using recursive formula
# def josephus_math(n,k):
#     result=[]
#     index=0
#     people=list(range(1,n+1))
#     for _ in range(n):
#         index=(index+k-1)%len(people)
#         result.append(str(people.pop(index)))
#     return "<"+",".join(result)+">"
# n,k=map(int,input().split())
# print(josephus_math(n,k))
#problem 3 Maze Representation
def bfs_queue(maze,N,M,x1,y1,x2,y2):
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    queue=deque([(x1,y1)])
    visited=[[False]*M for _ in range(N)]
    visited[x1][y1]=True
    while queue:
        x,y=queue.popleft()
        if(x,y)==(x2,y2):
            return "YES"
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and maze[nx][ny]==0 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))
    return "NO"
N,M=map(int,input('N M: ').split())
maze=[list(map(int,input(f'{i}번째 줄 미로 작성: ').split())) for i in range(N)]
x1,y1=map(int,input('출발(x1,y1): ').split())
x2,y2=map(int,input('도착(x2,y2): ').split())