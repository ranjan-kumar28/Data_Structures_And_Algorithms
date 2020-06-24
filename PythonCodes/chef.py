s=input().split()
rows=int(s[0])
cols=int(s[1])
lists=list()
space=False
alpha=False
for count in range(rows):
    lists.append(input())
count=0
for coln in range(cols):
    for l in lists:
        if l[coln].isalpha():
            print(l[coln],end='')
            row=l
            col=coln
            space=False
        if not l[coln].isalpha() and l[coln]!=' ':
            if space==False:
                print(' ',end='')
                space=True
ind=lists.index(row)
coln=0
for coln in range(cols):
    for r in range(rows):
        if coln>=col and r>=ind:
            print()
