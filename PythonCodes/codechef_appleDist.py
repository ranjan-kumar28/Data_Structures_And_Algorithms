
# n apples
# k boxes
try:
    testCases = int(input())
    for _ in range(testCases):
        n,k = map(int,input().split())
        boxes1 = [0]*k
        boxes2 = [0]*k
        
        apples = n
        #first candidate
        while(apples):
            boxes1 = [x+1 for x in boxes1]
            apples-=k

        #second candidate
        apples = n
        while(apples):
            minValue = min(boxes2)
            ind = boxes2.index(minValue)
            boxes2[ind] += k
            apples -= k
        if boxes1 == boxes2:print("NO")
        else:print("YES")
except:pass
