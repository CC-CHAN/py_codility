def solution(A):
    N = len(A)
    zeroCount = 0
    l = [0] * N
    for x in range(1, N):
        if(A[x-1]==0):
            zeroCount +=1
        if(A[x]==1):
            l[x] += zeroCount
    result = sum(l)
    return -1 if result > 1000000000 else result
