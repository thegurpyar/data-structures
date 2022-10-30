def kmpmatching(text,pattern):
    n=len(text)
    m=len(pattern)
    lps=[0]*m
    computeLPSarray(pattern,m,lps)
    i=0
    j=0
    
    while i<n:
        if text[i]==pattern[j]:   #if pattern matches
            i+=1
            j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                j=0
        if j==m:
            print(i-j)
            #if continue search
            #j=lps[j-1]