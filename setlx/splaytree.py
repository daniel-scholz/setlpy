from .tree import Tree
from .node import BinaryNode
from .splaynode import SplayNode


class SplayTree(Tree):
    """ordered binary trees with splaying algorithm"""

    def __init__(self, key=None, value=None):
        super().__init__(key, value)

    def insert(self, key, value=None):
        if not isinstance(key, SplayNode):
            node = SplayNode(key, value)
        else:
            node = key
        super().insert(node)
        self.splay(node)

    def find(self, node):
        result = super().find(node)
        if result != None:
            self.splay(node)
        return result
    #####################################################################
    #   ZIG: rechts
    #   ZAG: links
    #####################################################################

    def splay(self, node):
        if self.root != None and node != self.root.key:
            while self.root.key != node.key:
                self.root.splay(node)

    def _zig_rot(self, node):  # rechts rotation mit knoten LINKS unter der wurzel
        """
                  root                         node 
              /           \                 /       \
            node        root.right ==>  node.left   root
            /   \                                 /     \
    node.left   node.right                    node.right root.right
        """
        old_right = node.right  # save node's right sub tree

        node.right = self.root
        node.right.left = old_right  # old_root
        self.root = node

    def _zag_rot(self, node):  # links rotation mit knoten RECHTS unter der wurzel
        old_left = node.left  # save node's left sub tree

        node.left = self.root
        node.left.right = old_left  # old_root
        self.root = node

    def _zig_zag_rot(self, node):
        """
        rechts-links-rotation; knoten ist linkes kind von rechtem kind

                root # grand_parent                 
            /       \                                      node
        root.left   root.right # parent            /                \     
                      /  \                  ==> root            root.right
                node     root.right.right      /    \              /\
                /  \                     root.left   node.left    node.right|root.right.right
            node.left node.right
        """
        g = self.root
        p = self.root.right
        old_right = node.right

        node.right = p
        p.left = old_right
        # p = node

        old_left = node.left
        node.left = g
        g.right = old_left

        self.root = node

    def _zag_zig_rot(self, node):
        g = self.root
        p = self.root.left
        old_left = node.left

        node.left = p
        p.right = old_left
        # p = node

        old_right = node.right
        node.right = g
        g.left = old_right

        self.root = node

    def _zig_zig_rot(self, node):
        """
        first rotate grand-p and parent and THEN parent and node
                    root                                    node
            /                   \                      /         \
           root.left         root.right          node.left      root.left #parent
           /    \                       ==>                     /       \
        node    root.left.right                            node.right    root
        /   \                                                           /   \
node.left   node.right                                    root.left.right   root.right    
        """
        g = self.root
        p = self.root.left
        old_p_right = p.right
        p.right = g
        g.left = old_p_right
        # g = p

        old_right = node.right
        node.right = p
        p.left = old_right
        self.root = node

    def _zag_zag_rot(self, node):
        g = self.root
        p = self.root.right
        old_p_left = p.left
        p.left = g
        g.right = old_p_left
        # g = p

        old_left = node.left
        node.left = p
        p.right = old_left
        self.root = node
