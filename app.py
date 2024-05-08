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
    
x = Tree([1, 4, 6, 8, 3, 9, 12])

def pretty_print(node, prefix="", is_left=True):
    if node is None:
        return

    pretty_print(node.right, prefix + ("|   " if is_left else "    "), False)

    print(f"{prefix}{'`-- ' if is_left else '+-- '}{node.data}")

    pretty_print(node.left, prefix + ("    " if is_left else "|   "), True)

pretty_print(x.insert(x.root, 7))
# print(x.insert(7))
