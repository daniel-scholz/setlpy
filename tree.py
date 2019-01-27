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
        if self.root != None:
            if self.root.key == key:
                self.root.key = None
                if self.root.right != None:
                    self.root = self.root.right.find_min()
                elif self.root.left != None:
                    self.root = self.root.left
                return 
            return self.root.delete(key)

        raise ValueError(f"key {key} not found in tree")

    def __str__(self):
        if self.root != None:
            return str(self.root)
        return "[]"

