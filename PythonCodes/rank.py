# Enter your code here. Read input from STDIN. Print output to STDOUT
z=input().split()
n,m=int(z[0]),int(z[1])
for i in range(n):
    for j in range(m):
        
        #condition for welcome
        if i==int(n/2) and j>=int((m-7)/2) and j<(int((m-7)/2)+6):
            print("WELCOME",end='')
            for bn in range(int((m-7)/2)):
                print('-',end='')
            break

        
        print('-',end='')
    print('\n')
