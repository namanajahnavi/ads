class treenode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)
root.right.left=treenode(6)
root.right.right=treenode(7)

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root) :
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root) :
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

print("pre order : ")        
preorder(root)

print("in order : ")        
inorder(root)

print("post order : ")        
postorder(root)