class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, values):
        self.root = self.buildTree(values)

    def buildTree(self, values):
        arr = list(set(sorted(values)))

        if not arr:
            return None
        
        mid = len(arr) // 2
        root = Node(arr[mid])

        root.left = self.buildTree(arr[:mid])
        root.right = self.buildTree(arr[mid + 1:])

        return root
    
    def insert(self, root, value):
        if root is None:
            return Node(value)
        else:
            if root.data < value:
                root.right = self.insert(root.right, value)
            else:
                root.left = self.insert(root.left, value)
        return root
        
    def delete(self, root, value):
        if root is None:
            return None
        
        if value < root.data:
            root.left = self.delete(root.left, value)
        elif value > root.data:
            root.right = self.delete(root.right, value)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            root.data = curr.data
            root.right = self.delete(root.right, root.data)

    def find(self, root, value):
        if root == None:
            return False
        if root.data == value:
            return root.data
        
        if value < root.data:
            return self.find(root.left, value)
        else:
            return self.find(root.right, value)

    def levelOrder(self, root):
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            print(queue[0].data)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    def preOrder(self, root):
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)

    def depth(self, root):
        if root == None:
            return 0
        
        l = self.depth(root.left)
        r = self.depth(root.right)
        return max(l, r) + 1
    
x = Tree([1, 4, 6, 8, 3, 9, 12])

def pretty_print(node, prefix="", is_left=True):
    if node is None:
        return

    pretty_print(node.right, prefix + ("|   " if is_left else "    "), False)

    print(f"{prefix}{'`-- ' if is_left else '+-- '}{node.data}")

    pretty_print(node.left, prefix + ("    " if is_left else "|   "), True)
