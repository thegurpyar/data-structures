def bwt(s):
    matrix=[s]#inital banana$
    for i in range(1,len(s)):
        s=s[-1]+s[:-1]   #$+banana  #also updating s
        matrix.append(s)
    matrix.sort()
    b=""

    for i in range(len(s)):
        b+=matrix[i][-1]
    return b

s="banana$"
print(bwt(s))