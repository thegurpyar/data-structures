#find is used for finding representative
#union is used for making combining
p=[0]*13
for i in range(0,13):
    p[i]=i
print(p)
# for i in range(len(n)):
#     p[i]=i          #parent array as indexs

def find(x):
    if p[x]==x:
        return x
    else:
        return find(p[x])

def Union(a,b):
    x=find(a)
    y=find(b)
    if x==y:
        return
    else:
        p[y]=x



Union(2, 10)
Union(7, 5)
Union(6, 1)
Union(3, 4)
Union(5, 11)
Union(7, 8)
Union(7, 3)
Union(12, 2)
Union(9, 6)
print(p)
print(find(6))
print(find(3))
print(find(11))
print(find(9))