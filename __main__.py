from setlx.tree import Tree
from setlx.node import BinaryNode


root = BinaryNode(10)
tree = Tree(root)
print(tree)
tree.insert(BinaryNode(7))
print(tree)
tree.insert(BinaryNode(6))
# print(tree)
tree.insert(BinaryNode(8))
tree.insert(BinaryNode(2.3))
tree.insert(BinaryNode(13))
tree.insert(BinaryNode(11))
tree.insert(BinaryNode(12))
tree.insert(BinaryNode(18))
# print(tree)
tree.delete(7)
print(tree)
tree.delete(18)
print(tree)
