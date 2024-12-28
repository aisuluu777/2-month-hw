
import random

def start_game(min_number, max_number, chances,capital):

    target = random.randint(min_number, max_number)


    print(f'Добро пожаловать в игру!')
    print(f'Вам нужно угадать число от {min_number} до {max_number}.')
    print(f'У вас {chances} попыток и начальный капитал. {capital}.')

    for chance in range(1,chances + 1):
        if capital <= 0:
            print('У вас не хватает средств! Игра окончена.')
            break

        print(f'Попытка {chance} из {chances}. Ваш капитал: {capital} монет.')

        try:
            money = int(input('Введите вашу ставку: '))
            if money <= 0 or money > capital:
                print('Недастаточно средств или средства превышает капитал!')
                continue

            user_guess = int(input(f'Введите число от {min_number} до {max_number}: '))

            if user_guess == target:
                capital += money * 2
                print(f'Ура вы выиграли! {target} и выиграли {money} монет!')
                break
            else:
                capital -= money
                if user_guess < target:
                    print('Больше')
                else:
                    print('Меньше')

        except ValueError:
            print('Ошибка ввода! Пожалуйста, введите число.')

        print(f'Игра окончена. Ваш итоговый капитал: {capital} монет.')
