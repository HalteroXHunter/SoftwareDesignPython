from toyfactory import ToyFactory
from playaction import RollPlay, FlyPlay
from sound import EngineSound, ChooChooSound

if __name__ == '__main__':
    roll_play = RollPlay()
    fly_play  = FlyPlay()
    
    engine_sound    = EngineSound()
    choo_choo_sound = ChooChooSound()

    #         ToyCar        ModelAirplane  TrainSet
    plays  = [roll_play,    fly_play,      roll_play]
    sounds = [engine_sound, engine_sound,  choo_choo_sound]
    
    for toy_class, play, sound \
            in zip(ToyFactory.toy_classes, plays, sounds):
        toy = ToyFactory.make(toy_class, play, sound)
        print(toy)
