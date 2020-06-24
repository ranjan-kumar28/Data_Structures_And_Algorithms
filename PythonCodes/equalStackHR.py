def equalStacks(h1, h2, h3):
    s1=0
    s2=1
    s3=2
    while(not (s1==s2==s3)):
        s1=sum(h1)
        s2=sum(h2)
        s3=sum(h3)
        print(h1,h2,h3,s1,s2,s3)
        if(s1==0 or s2==0 or s3==0):break
        if(s1>s2 or s1>s3):
            h1.pop(0)
        if(s2>s3 or s2>s1):
            h2.pop(0)
        if(s3>s1 or s3>s2):
            h3.pop(0)
    if(s1==0 or s2==0 or s3==0):print(0)
    else:print(s1)
