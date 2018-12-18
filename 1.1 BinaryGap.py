def solution(N):
    num = str(bin(N)).strip('0b')
    myList = num.split('1')
    if not num.endswith('1'):
        myList = myList[:-1]
    if(len(myList) < 1):
        return 0
    return len(max(myList, key=len))
