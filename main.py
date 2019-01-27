from tree import Tree


class Node():
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.key},{self.value},{self.left},{self.right}]"

    def insert(self, node):
        if node.key > self.key:
            if self.right != None:
                return self.right.insert(node)
            self.right = node
        else:
            if self.left != None:
                return self.left.insert(node)
            self.left = node

    def find(self, key):
        if key == self.key:
            return self.value
        if key < self.key and self.left != None:
            return self.left.find(key)
        if key > self.key and self.right != None:
            return self.right.find(key)

    def delete(self, key):
        if self.left != None:
            node = self.left
            if key == node.key:
                if node.left == None:
                    node = node.right
                elif node.right == None:
                    node = node.left
                else:
                    node = node.right.find_min()
            elif node.left != None and key < node.key:
                node.left.delete(  key)
            elif node.right != None:
                node.right.delete(key)

        elif self.right != None:
            node = self.right
            if key == node.key:
                if node.left == None:
                    node = node.right
                elif node.right == None:
                    node = node.left
                else:
                    node = node.right.find_min()
            elif node.left != None and key < node.key:
                node.left.delete(key)
            elif node.right != None:
                node.right.delete(key)

    def find_min(self):
        return None


root = Node(10, 10, None, None)
tree = Tree(root)
tree.insert(Node(4, 4, None, None))
tree.insert(Node(11, 11, None, None))
tree.insert(Node(12, 12, None, None))
tree.insert(Node(6, 6, None, None))
print(tree)
print(tree.find(6))
print(tree.find(11))
print(tree.find(3))
print(tree)
tree.delete(4)
print(tree)
