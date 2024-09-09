class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def Insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return True

        
        temp = self.root
        while True:
            if new_node.data == temp.data:
                print("Node already exists")
                return False

            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def contains(self,data):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if data<temp.data:
                temp=temp.left
            elif data > temp.data:
                temp=temp.right
            else:
                return True
        return False
    def BMF(self):
        current=self.root
        if current is None:
            return []
        queue=[]
        result=[]
        queue.append(current)
        while len(queue) > 0:
            current=queue.pop(0)
            result.append(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return result
    def preorder(self):
        result=[]
        def traverse(current):
            result.append(current.data)
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)
        traverse(self.root)
        return result
    def postorder(self):
        result=[]
        def traverse(current):
            if current.left is not None:
                traverse(current.left)
            if current.right is not None:
                traverse(current.right)
            result.append(current.data)
        traverse(self.root)
        return result
    def inorder(self):
        result=[]
        def traverse(current):
            if current.left is not None:
                traverse(current.left)
                result.append(current.data)
            if current.right is not None:
                traverse(current.right)
        traverse(self.root)
        return result

# Test the code
MT = Tree()
MT.Insert(50)
MT.Insert(48)
MT.Insert(55)
MT.Insert(49)
MT.Insert(21)
MT.Insert(51)
MT.Insert(56)
print(MT.contains(21))
print(MT.contains(0))
print(MT.preorder())
print(MT.postorder())

