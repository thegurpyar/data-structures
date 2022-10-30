class TrieNode:
    def __init__(self,char):
        self.char=char
        self.children={}
        self.isend=False

class Trie:
    def __init__(self):
        self.root=TrieNode(",")

    def insert(self,data):
        node=self.root
        
        for char in data:
            temp=TrieNode(char)
            if char in node.children:
                node=node.children[char]
            else:
                node.children[char]=temp
                node=node.children[char]
        node.isend=True

    def search(self,word):
        currentnode=self.root
        for i in word:
            if i not in currentnode.children:
                return "String do not exist"
            else:
                currentnode=currentnode.children[i]
        if currentnode.isend==True:
            return "string exist"
        else:
            return "String exist as prefix of another"

            
def prefixmatching(text,trie):    #SIMPLE SI BAT H CHECK KR RAHA H KI PATTERN EXIST KRTA H
    v=trie.root
    for i in range(len(text)):
        if i in v.children:
            v=v.children[i]
        elif  v.children[i]==None:
                return True
        else:
            return False





t=Trie()
t.insert("AATCGGGTTCAATCGGGGT")
print(prefixmatching("AAC",t))
