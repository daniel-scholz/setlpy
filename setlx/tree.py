class Tree():
    def __init__(self, node):
        self.root = node

    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            self.root.insert(node)

    def find(self, key):
        if self.root != None:
            return self.root.find(key)

    def delete(self, key):
        tree = self
        if tree.root != None:
            root = tree.root
            if root.key == key:
                # check if right subtree is minimum
                if root.right == None:
                    tree.root = root.left
                elif root.left == None:
                    tree.root = root.right
                else:
                    root_right_child = root.right
                    if root_right_child.left == None:
                        root.right = root_right_child.right
                        root.key = root_right_child.key
                    else:
                        # parent.key = current.del_min()
                        root.key = root_right_child.del_min()
            else:
                tree.root.delete(key)
        else:
            raise ValueError(f"tree is empty")

    def __str__(self):
        if self.root != None:
            return str(self.root)
        return "[]"
