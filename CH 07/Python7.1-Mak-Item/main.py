from item import Item, OrganicItem

if __name__ == '__main__':
    peach = Item('peaches')
    peach.print_cost(2.99, 2)
    
    print()
    
    peach = OrganicItem('peaches', 25)
    peach.print_cost(2.99, 2)
