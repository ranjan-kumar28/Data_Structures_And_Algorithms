def power(a,b):
    if(not b):return 1
    
    temp = power(a,int(b/2))
    
    if(not b%2):return temp*temp
    
    else:
        if(b>0):return temp*temp*a
        else: return temp*temp/a
        
print(power(2,-2))
