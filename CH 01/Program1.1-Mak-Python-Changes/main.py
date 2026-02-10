from car import Car
from driver import Driver

if __name__ == '__main__':
    my_car = Car()
    driver = Driver(my_car)
    
    driver.start_car()