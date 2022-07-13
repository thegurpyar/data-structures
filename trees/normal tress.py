#general tree



class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self           #prent - child relationship
        self.children.append(child)
    
    # def print_tree(self):
    #     print(self.data)
    #     for child in self.children:
    #         child.print_tree()
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent

        print(level+1)   ##



def print_tree(root):
    print(root.data)
    for child in root.children:
        print_tree(child)



root=Node("electronics")

laptop=Node("laptops")

root.add_child(laptop)

macbook = Node("macbook")
laptop.add_child(macbook)

surface=Node("surface")
laptop.add_child(surface)

cellphones = Node("cellphones")

root.add_child(cellphones)

iphone=Node("iphone")

cellphones.add_child(iphone)

pixel=Node("pixel")

cellphones.add_child(pixel)

vivo = Node("vivo")

cellphones.add_child(vivo)

tv=Node("tv")

root.add_child(tv)

samsung = Node("samsung")

tv.add_child(samsung)

lg=Node("lg")

tv.add_child(lg)

lg.get_level()
# get_height(root)