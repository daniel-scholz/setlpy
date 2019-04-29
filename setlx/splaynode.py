import copy

from .node import Node, _Key


class SplayNode(Node):
    def __init__(self, key, left=None, right=None):
        if isinstance(key, Node):
            right = key.right
            left = key.left
            key = key.key
        super().__init__(key=key, left=left, right=right)

    def splay(self, node):
        if self is not None and _Key(node.key) != _Key(self.key):
            if self.left is not None:
                if _Key(self.left.key) == _Key(node.key):  # node ist links unter der wurzel
                    self._zig_rot(self.left)
                elif self.left.right is not None and _Key(self.left.right.key) == _Key(node.key):
                    # erst rechts dann links
                    self._zag_zig_rot(self.left.right)
                elif self.left.left is not None and _Key(self.left.left.key) == _Key(node.key):
                    self._zig_zig_rot(self.left.left)
            if self.right is not None:
                if _Key(self.right.key) == _Key(node.key):  # node ist rechts unter der wurzel
                    self._zag_rot(self.right)
                elif self.right.left is not None and _Key(self.right.left.key) == _Key(node.key):
                    self._zig_zag_rot(self.right.left)
                elif self.right.right is not None and _Key(self.right.right.key) == _Key(node.key):
                    self._zag_zag_rot(self.right.right)
            if self.left is not None and _Key(node.key) < _Key(self.key):
                self.left.splay(node)
            elif self.right is not None:
                self.right.splay(node)

    def _zig_rot(self, node):  # right rotation mit node LINKS below der wurzel
        """
                  root                         node
              /           \                 /       \
            node        root.right ==>  node.left   root
            /   \                                 /     \
    node.left   node.right                    node.right root.right
        """
        old_right = node.right  # save node's right sub tree

        node.right = SplayNode(self)
        # node.right = self
        node.right.left = old_right  # old_root
        self.key = node.key
        self.left = node.left
        self.right = node.right

    def _zag_rot(self, node):  # links rotation mit knoten RECHTS unter der wurzel
        old_left = node.left  # save node's left sub tree

        node.left = copy.deepcopy(self)
        node.left.right = old_left  # old_root
        self.key = node.key
        self.left = node.left
        self.right = node.right

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
        g = SplayNode(self)
        p = SplayNode(self.right)
        old_right = node.right

        node.right = p
        p.left = old_right
        # p = node

        old_left = node.left
        node.left = g
        g.right = old_left

        self.key = node.key
        self.left = node.left
        self.right = node.right

    def _zag_zig_rot(self, node):
        g = SplayNode(self)
        p = SplayNode(self.left)
        old_left = node.left

        node.left = p
        p.right = old_left
        # p = node

        old_right = node.right
        node.right = g
        g.left = old_right

        self.key = node.key
        self.left = node.left
        self.right = node.right

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
        g = SplayNode(self)
        p = SplayNode(self.left)
        old_p_right = p.right
        p.right = g
        g.left = old_p_right
        # g = p

        old_right = node.right
        node.right = p
        p.left = old_right
        self.key = node.key
        self.left = node.left
        self.right = node.right

    def _zag_zag_rot(self, node):
        g = SplayNode(self)
        p = SplayNode(self.right)
        old_p_left = p.left
        p.left = g
        g.right = old_p_left
        # g = p

        old_left = node.left
        node.left = p
        p.right = old_left
        self.key = node.key
        self.left = node.left
        self.right = node.right
