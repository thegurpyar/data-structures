n=[0,1,2,0,4,5,6,7]
p=[0]*len(n)
for i in range(len(n)):
    p[i]=i
              #parent array as indexs
def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[i]


print(find(3))

