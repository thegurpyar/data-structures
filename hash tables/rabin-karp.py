
def get_hash(key):
    sums=0
    for i in range(len(key)):               
        sums+=(ord(key[i])*(10**i))%101
    return sums



def rbk(text,pattern):
    if len(pattern)>len(text):
        return -1
        
    patternhash=0
    texthash=0
    for i in range(len(pattern)):     #hash for pattern and first window
        patternhash+=get_hash(pattern[i])
        texthash+=get_hash(text[i])

    for i in range(len(text)-len(pattern)+1):
        
        if patternhash==texthash:
            for j in range(len(pattern)):
                if pattern[j]!=text[j+i]:   # for next idx in text
                    break
                
            j+=1                # +1 for length of pattern
            
            if j==len(pattern):
                return("pattern found "+str(i))
                

        if i < len(text)-len(pattern):
            
            texthash=texthash-get_hash(text[i])+get_hash((text[i+len(pattern)]))

    

print(rbk("FOUR","UR"))
# print(ord("F")+ord("O"))
# # print(ord("F"))
# print(ord("R"))
