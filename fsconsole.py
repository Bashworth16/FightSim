
import time
from fightsim import *


def slow_print(string):
    for each in string:
        time.sleep(0.04)
        print(each, end='')
    print("")


def attack_format(a, b):
    if b.health < -10:
        slow_print(f'{a.name} Punched {b.name} for {a.atk} DAMAGE!!!')
        slow_print("OVERKILL K.O.!!!")
    else:
        slow_print(f'{a.name} Punched {b.name} for {a.atk} DAMAGE!!!')
    return


def winner_format(x):
    slow_print(f'THE WINNER IS {x.name}!!!')


def format_health(player):
    slow_print(f'{player.name}: 😬 {player.health} 😤')


def block_format(player1, player2):
    slow_print(f"{player1.name} Blocked {player2.name}'s attack!")


def attack_phase(player1, player2):
    slow_print(f'{player1.name} is attacking with {player1.atk}')
    if block() is True:
        block_format(player2, player1)
        return
    else:
        player2.health = attack(player1.atk, player2.health)
        attack_format(player1, player2)
        format_health(player2)
        return


def get_winner(a, b):
    if check_die(a.health) is True:
        return winner_format(b)
    if check_die(b.health) is True:
        return winner_format(a)
    else:
        return


def swing(player1, player2):
    if coin_flip() is True:
        return attack_phase(player1, player2)
    else:
        return attack_phase(player2, player1)


def get_round(r, rot):
    if rot % 4 is 0:
        r += 1
        print("")
        slow_print(f'ROUND {r}! FIGHT!')
        return r
    else:
        return r


def check_state(player1, player2):
    if check_play(player1, player2) is False:
        return False
    else:
        return True


def main():
    funk = Player(name="FunkFoo", health=100, atk=random.randint(1, 50))
    foo = Player(name="FuuBar", health=100, atk=random.randint(1, 50))
    round_count = 1
    rotation_count = 0
    slow_print(f'ROUND {round_count}! FIGHT!')
    while True:
        funk.atk = random.randint(1, 50)
        foo.atk = random.randint(1, 50)
        rotation_count += 1
        round_count = get_round(round_count, rotation_count)
        swing(funk, foo)
        get_winner(funk, foo)
        if check_state(funk, foo) is False:
            break
        else:
            continue

    slow_print("Goodbye!")
    return


if __name__ == '__main__':
    main()
