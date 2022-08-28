def substring(str,pattern):
    found=[]
    for i in range(len(str)-len(pattern)+(1)):
        stridx=i
        patternidx=0
        
        while stridx < len(str) and patternidx < len(pattern) and str[stridx]==pattern[patternidx]:
            found.append(stridx)
            stridx+=1
            patternidx+=1
            
        if patternidx==len(pattern):
            return found

print(substring("hashing","ing"))