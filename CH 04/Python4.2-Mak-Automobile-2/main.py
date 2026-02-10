from automobile import Automobile, Garage, CarWash

if __name__ == '__main__':
    auto = Automobile()
    auto.accelerate()
    
    garage = Garage(auto)
    garage.change_oil()
    
    carwash = CarWash(auto)
    carwash.wash_car()