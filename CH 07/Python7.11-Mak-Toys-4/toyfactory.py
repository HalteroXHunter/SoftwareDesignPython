from toy import ToyCar, ModelAirplane, TrainSet

class ToyFactory:    
    toy_classes = [ToyCar, ModelAirplane, TrainSet]
    
    @staticmethod
    def make(toy_type, play, sound):
        return toy_type(play, sound)
