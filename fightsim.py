
from slowprint.slowprint import *
import random


class Player:
    def __init__(self, name, health, atk):
        self.name = name
        self.health = health
        self.atk = atk


def attack_format(a, b):
    slowprint(f'{a.name} Punched {b.name} for {a.atk} DAMAGE!!!', .12)
    return


def attack(p1a, p2h):
    p2h = p2h - p1a
    return p2h


def attack_phase(player1, player2):
    player2.health = attack(player1.atk, player2.health)
    if block() is True:
        block_format(player2, player1)
        return
    attack_format(player1, player2)
    format_health(player2)


def check_die(player):
    if player < 0 or player == 0:
        return True
    else:
        return False


def winner_format(x):
    slowprint(f'THE WINNER IS {x.name}!!!', 0.9)


def get_winner(a, b):
    if check_die(a.health) is True:
        return winner_format(b)
    if check_die(b.health) is True:
        return winner_format(a)
    else:
        return


def format_health(player):
    slowprint(f'{player.name}: 😬 {player.health} 😤', 0.9)


def check_play(player1, player2):
    if check_die(player1.health) is True:
        return False
    if check_die(player2.health) is True:
        return False
    else:
        return True


def block_format(player1, player2):
    slowprint(f"{player1.name} Blocked {player2.name}'s attack!", 0.8)


def block():
    chance = ['Hit', 'Block']
    luck = random.randint(0, (len(chance)))
    if luck is 0:
        return False
    if luck is 1:
        return True


def main():
    funk = Player("FunkFoo", 100, 10)
    foo = Player("FuuBar", 100, 10)
    turn_count = 1
    rotation_count = 0
    slowprint(f'ROUND {turn_count}! FIGHT!', 0.1)
    while True:
        rotation_count += 1
        if rotation_count % 2 is 0:
            turn_count += 1
            print("")
            slowprint(f'ROUND {turn_count}! FIGHT!', 0.1)
        attack_phase(funk, foo)
        get_winner(funk, foo)
        if check_play(funk, foo) is False:
            break
        attack_phase(foo, funk)
        get_winner(funk, foo)
        if check_play(funk, foo) is False:
            break
        else:
            continue
    print("Goodbye!")
    return


if __name__ == '__main__':
    main()
