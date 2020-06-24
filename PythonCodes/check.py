def remove_duplicates(l):
  n=[]
  x=0
  for i in range(len(l)):
    for j in range(len(l)):
      if l[i]==l[j] and i!=j:
      	x=l[i]
    n.append(x)
  return n
print(remove_duplicates([1,2,2,3,4,6,6]))
