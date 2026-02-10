from sports import Baseball, Football, Volleyball

def generate_report(sport):
    print(sport.SPORT_TYPE)
    print(f'  players: {sport.recruit_players()}')
    print(f'    venue: {sport.reserve_venue()}')
    print()

if __name__ == '__main__':
    for sport in [Baseball(), Football(), Volleyball()]:
        generate_report(sport)
