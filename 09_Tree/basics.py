import sys
class Node:
    def __init__(self,x) :
        self.val=x
        self.children=[]

def addChild(parent, child):
    parent.children.append(child)

def printParents(node,parent):
    if parent is None:
        print(str(node.val)+" -> Null")
    else:
        print(str(node.val)+" ->  "+ str(parent.val))

    for child in node.children:
        printParents(child,node)
def printChildren(node):
    children_str=' '.join(str(child.val) for child in node.children)
    print(str(node.val)+'->'+children_str)
    for child in node.children:
        printChildren(child)

def printLeafNodes(node):
    if not node.children:
        sys.stdout.write(str(node.val)+" ")
        return
    for child in node.children:
        printLeafNodes(child)

def printDegrees(node, parent):
    degree=len(node.children)
    if parent is not None:
        degree+=1
    print(str(node.val)+"->"+str(degree))
    for child in node.children:
        printDegrees(child,node)

if __name__=='__main__':
    root=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)

# Constructing tree 
    addChild(root,n2)
    addChild(root,n3)
    addChild(n2,n4)
    addChild(n2,n5)

    print("Parents of each node")
    printParents(root,None)

    print("Children of each node")
    printChildren(root)

    print("Leaf nodes:")
    printLeafNodes(root)
    print('\n')

    print("Degrees of nodes:")
    printDegrees(root, None)