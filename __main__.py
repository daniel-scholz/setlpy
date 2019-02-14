from tree import Tree


class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.key},{self.left},{self.right}]"

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
            return self.key
        if key < self.key and self.left != None:
            return self.left.find(key)
        if key > self.key and self.right != None:
            return self.right.find(key)

    def delete(self, key):
        parent =self
        if parent.left and key < parent.key:
            current = parent.left
            if current.key == key:
                if current.right == None:
                    parent.left = current.left
                elif current.left == None:
                    parent.left = current.right
                else:
                    current.key = parent.del_min()
            else:
                current.delete(key)
        elif parent.right and key > parent.key:
            current = parent.right
            if current.key == key:
                if current.right == None:
                    parent.right = current.left
                elif current.left == None:
                    parent.right = current.right
                else:
                    current.key = parent.del_min()
            else:
                current.delete(key)

    def del_min(self) -> int:
        """
            Returns value of minimum of subtree self
            Deletes node of minimum value
        """
        parent = self
        current = parent.left
        nxt = current.left
        if nxt == None:
            k = current.key
            parent.left = current.right
            return k
        else:
            return current.del_min()


root = Node(10)
tree = Tree(root)
print(tree)
tree.insert(Node(7))
print(tree)
tree.insert(Node(6))
# print(tree)
tree.insert(Node(8))
tree.insert(Node(15))
tree.insert(Node(13))
tree.insert(Node(11))
tree.insert(Node(12))
tree.insert(Node(18))
# print(tree)
tree.delete(7)
print(tree)
tree.delete(18)
print(tree)

