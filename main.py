from decouple import config
from logic import start_game
def load_config():

    min_num = config('MIN_NUMBER', cast=int)
    max_num = config('MAX_NUMBER', cast=int)
    chance = config('CHANCES', cast=int)
    capital = config('START_UP_CAPITAL', cast=int)
    return min_num, max_num,chance ,capital






if __name__ == '__main__':
    min_num, max_num,chance ,capital = load_config()

    start_game(min_num, max_num, chance, capital)


