from toy import ToyCar, ModelAirplane, TrainSet
from playaction import RollPlay, FlyPlay
from sound import EngineSound, ChooChooSound

if __name__ == '__main__':
    car = ToyCar(RollPlay(), EngineSound())
    print(car)
    
    plane = ModelAirplane(FlyPlay(), EngineSound())
    print(plane)
    
    train = TrainSet(RollPlay(), ChooChooSound())
    print(train)
    
    train.sound = EngineSound()
    print(train)
