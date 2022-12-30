class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)