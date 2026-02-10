from item import Item

if __name__ == '__main__':
    item = Item('whole chicken', 4.5, 10.31)
    
    print(f'  name: {item.name}')
    print(f'weight: {item.weight}')
    print(f' price: ${item.price}')
    print()
    
    item.price = 10.75
    print(f'new price: ${item.price}')  
    print()  
    
    item.price = -9.99
    print(f'new price: ${item.price}')