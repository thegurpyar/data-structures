def LPS(s):

     lps=[0]*len(s)
     lps[0]=0
     previous=0
     i=1

     while i<len(s):

        if s[i]==s[previous]:  #match   pre==suf
            lps[i]=previous+1
            previous+=1
            i+=1
     return lps



s="AAA"
print(LPS(s))