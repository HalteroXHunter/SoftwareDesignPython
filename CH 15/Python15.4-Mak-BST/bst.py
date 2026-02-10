from node import Node

class BST:
    def __init__(self):
        self._root = None
    
    def insert(self, value):
        self._root = self._insert(value, self._root)
        
    def _insert(self, value, node):
        if node is None:
            return Node(value)  
                 
        if value <= node.value:
            node.left = self._insert(value, node.left)        
        else:
            node.right = self._insert(value, node.right)
            
        return node
            
    def print_tree(self):
        self._print_tree(self._root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(f'{node.value:3d}', end='')
            self._print_tree(node.right)
