from slowprint.slowprint import *
from fightsim import *


def attack_format(a, b):
    slowprint(f'{a.name} Punched {b.name} for {a.atk} DAMAGE!!!', .12)
    return


def winner_format(x):
    slowprint(f'THE WINNER IS {x.name}!!!', 0.9)


def format_health(player):
    slowprint(f'{player.name}: 😬 {player.health} 😤', 0.9)


def block_format(player1, player2):
    slowprint(f"{player1.name} Blocked {player2.name}'s attack!", 0.8)


def attack_phase(player1, player2):
    if block() is True:
        block_format(player2, player1)
        return
    else:
        player2.health = attack(player1.atk, player2.health)
        # FIX THIS
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


def main():
    funk = Player("FunkFoo", 100, 10)
    foo = Player("FuuBar", 100, 10)
    round_count = 1
    rotation_count = 0
    slowprint(f'ROUND {round_count}! FIGHT!', 0.1)
    while True:
        rotation_count += 1
        if rotation_count % 2 is 0:
            round_count += 1
            print("")
            slowprint(f'ROUND {round_count}! FIGHT!', 0.1)
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
