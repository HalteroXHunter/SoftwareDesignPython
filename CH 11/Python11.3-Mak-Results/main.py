from intramural import Intramural
from sport import SportType, Sport
from game import Game
from hall import HallName, Hall

def build_tree():
    intramural = Intramural()
    
    baseball   = Sport(SportType.BASEBALL)
    football   = Sport(SportType.FOOTBALL)
    volleyball = Sport(SportType.VOLLEYBALL)
    
    intramural.add_sport(baseball)
    intramural.add_sport(football)
    intramural.add_sport(volleyball)
    
    north = Hall(HallName.NORTH)
    south = Hall(HallName.SOUTH)
    east  = Hall(HallName.EAST)
    west  = Hall(HallName.WEST)
    
    intramural.add_hall(north)
    intramural.add_hall(south)
    intramural.add_hall(east)
    intramural.add_hall(west)
    
    baseball.add_game(Game(west, 5, east,  3))
    baseball.add_game(Game(east, 3, south, 0))
    
    football.add_game(Game(north, 27, west, 21))
    
    volleyball.add_game(Game(west,  15, south, 10))
    volleyball.add_game(Game(north, 15, south, 13))
    volleyball.add_game(Game(south, 15, west,  14))
    
    return intramural

if __name__ == '__main__':
    intramural = build_tree()
    
    intramural.print_scores_report()
    intramural.print_activities_report()
    intramural.print_winnings_report()
    