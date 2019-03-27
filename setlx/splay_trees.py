from .tree import Tree
from .node import BinaryNode


class SplayTree(Tree):
    """ordered binary trees with splaying algorithm"""

    def __init__(self, node=None):
        super().__init__(node)

    def insert(self, node):
        super().insert(node)
        # print(" vor splaying:", self)
        self.splay(node)
        # print("nach splaying:", self)

    def find(self, node):
        super().find(node)
        self.splay(node)

    #####################################################################
    #   ZIG: rechts
    #   ZAG: links
    #####################################################################

    def splay(self, node):
        if self.root != None and node != self.root.key:
            if self.root.left != None:
                if self.root.left.key == node:  # node ist links unter der wurzel
                    self._zig_rot(self.root.left)
                elif self.root.left.right != None and self.root.left.right.key == node:
                    # erst rechts dann links
                    self._zag_zig_rot(self.root.left.right)
                elif self.root.left.left != None and self.root.left.left.key == node:
                    self._zig_zig_rot(self.root.left.left)
            if self.root.right != None:
                if self.root.right.key == node:  # node ist rechts unter der wurzel
                    self._zag_rot(self.root.right)
                elif self.root.right.left != None and self.root.right.left.key == node:
                    self._zig_zag_rot(self.root.right.left)
                elif self.root.right.right != None and self.root.right.right.key == node:
                    self._zag_zag_rot(self.root.right.right)
        else:
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
