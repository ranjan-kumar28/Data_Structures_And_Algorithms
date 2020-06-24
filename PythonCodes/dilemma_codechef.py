# 1 face up card
# 0 face down card
# -1 card removed
try:
    for _ in range(int(input())):
        row = list(map(int,str(input())))
        status = ''
        while(1 in row):
            ind = row.index(1)
            if len(row)==1 and row[0]==1:
                row[0]=-1
            elif not ind and len(row)>1:
                row[ind] = -1
                if not row[ind+1]:row[ind+1]=1
                elif row[ind+1]==1:row[ind+1]=0
                elif row[ind+1]==-1:continue
            elif ind+1 == len(row) and len(row)>1:
                row[ind] = -1
                if not row[ind-1]:row[ind-1]=1
                elif row[ind-1]==1:row[ind-1]=0
                elif row[ind-1]==-1:continue
            elif len(row)>1 and ind!=0 and ind+1!=len(row):
                row[ind]=-1
                if not row[ind+1]:row[ind+1]=1
                elif row[ind+1]==1:row[ind+1]=0
                if not row[ind-1]:row[ind-1]=1
                elif row[ind-1]==1:row[ind-1]=0
        status = 'WIN'
        for card in row:
            if card!=-1:status='LOSE'
        print(status)
except:pass
