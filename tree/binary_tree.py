class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return 
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def inorderTraversal(self):
        elements=[]
        if self.left:
            elements += self.left.inorderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorderTraversal()
        return elements
        
        
def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
        
if __name__=='__main__':
    numbers = [17,21,8,4,74,2,30,13,5,14]
    numbers_tree = buildTree(numbers)
    print(numbers_tree.inorderTraversal())
