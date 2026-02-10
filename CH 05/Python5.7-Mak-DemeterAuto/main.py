from auto import Sparkplug, Engine, DemeterAuto

if __name__ == '__main__':
    sparkplug = Sparkplug('main')
    engine = Engine(sparkplug)
    
    demeter_auto = DemeterAuto(engine)
    demeter_auto.maintain_auto()