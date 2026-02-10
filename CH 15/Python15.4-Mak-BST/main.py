import random
from bst import BST

TREE_SIZE = 20

if __name__ == '__main__':
    tree = BST()
    
    print('Inserting:', end='')
    for _ in range(TREE_SIZE):
        value = random.randint(0, 99)
        print(f'{value:3d}', end='')
        tree.insert(value)
       
    print() 
    print(' Printing:', end='')
    tree.print_tree()
    