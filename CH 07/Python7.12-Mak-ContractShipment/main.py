from shipment import Shipment
from expedited import Expedited
from international import International
from exceptions import CostException, DaysException

def ship(shipment, *, cost):
    try:
        print(f'Shipping {shipment.kind}')
        print(f'  setting {cost = }')
                
        if cost >= 1:        
            shipment.cost = cost

        shipment.calculate_days()
        days = shipment.days
        
        if not (1 <= days <= 14):
            raise DaysException(days, 1, 14)
        
    except CostException as ex:
        print(f'*** Cost {ex.cost} violates cost precondition: '
              f'cost >= {ex.min_cost}')
    except DaysException as ex:
        print(f'*** Days {ex.days} violates days postcondition: '
              f'{ex.min_days} <= days <= {ex.max_days}')
    else:
        print('Shipped OK!')
        
    print()

if __name__ == '__main__':
    ship(Shipment(),      cost=2)
    ship(Expedited(),     cost=4)
    ship(International(), cost=11)
