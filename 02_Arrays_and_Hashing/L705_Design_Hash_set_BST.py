class TreeNode:
    def __init__(self, data) -> None:
        self.data=data
        self.left_node=None
        self.right_node=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self, root, data):
        if not root:
            return TreeNode(data)
        if data<root.data:
            root.left_node=self.insert(root.left_node,data)
        elif data> root.data:
            root.right_node=self.insert(root.right_node, data)
        return root

    def search(self, root, data):
        if not root:
            return False
        if root.data==data:
            return True
        elif data<root.data:
            return self.search(root.left_node,data)
        else:
            return self.search(root.right_node,data)

    def delete(self,root,data):
        if not root:
            return None 
        if data< root.data:
            root.left_node=self.delete(root.left_node,data)
        elif data > root.data:
            root.right_node=self.delete(root.right_node,data)
        else:
            if not root.left_node:
                return root.right_node
            if not root.right_node:
                return root.left_node
            temp=self.get_min_Val(root.right_node)
            root.data=temp.data
            root.right_node=self.delete(root.right_node,temp.data)
        return root
    
    def get_min_Val(self, root):
        while root.left_node:
            root=root.left_node
        return root


    def add(self,key):
        self.root=self.insert(self.root, key)
    
    def contains(self, key):
        return self.search(self.root,key)
    
    def remove(self, key):
        self.root= self.delete(self.root, key)
    

class MyHashSet:

    def __init__(self):
        self.b_size=10000
        self.bucket=[BinarySearchTree() for _ in range(self.b_size)]

    def hash(self,key):
        return key%self.b_size
    
    def add(self, key: int) -> None:
        idx=self.hash(key)
        if not self.contains(key):
            self.bucket[idx].add(key)

    def remove(self, key: int) -> None:
        idx=self.hash(key)
        if self.contains(key):
            self.bucket[idx].remove(key)


    def contains(self, key: int) -> bool:
        idx=self.hash(key)
        return self.bucket[idx].contains(key)