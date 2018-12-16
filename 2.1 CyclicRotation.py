from collections import deque

def solution(A, K):
    myDeque = deque(A)
    myDeque.rotate(K)
    return list(myDeque)
