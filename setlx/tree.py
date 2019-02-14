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
        parent = self
        if parent.root != None:
            current = parent.root
            if current.key == key:
                nxt = current.right
                # check if right subtree is minimum
                if nxt == None:
                    parent.root = current.left
                else:
                    parent = current
                    current = current.right
                    nxt = current.left
                    if nxt == None:
                        current.left = parent.left
                        parent = current
                    else:
                        parent.key = current.del_min()
            else:
                current.delete(key)
        else:
            raise ValueError(f"tree is empty")

    def __str__(self):
        if self.root != None:
            return str(self.root)
        return "[]"
