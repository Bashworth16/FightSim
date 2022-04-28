
import time
from fightsim import *


def slow_print(string):
    for each in string:
        time.sleep(0.05)
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
        return player2.name
    else:
        player2.health = attack(player1.atk, player2.health)
        attack_format(player1, player2)
        format_health(player2)
        return player1.name


def get_winner(a, b):
    if check_die(a.health) is True:
        winner_format(b)
        return True
    if check_die(b.health) is True:
        winner_format(a)
        return True
    else:
        return False


def swing(player1, player2):
    if coin_flip() is True:
        return attack_phase(player1, player2)
    else:
        return attack_phase(player2, player1)


def get_round(x, p1, y, p2, r, rot):
    togo1 = x - p1.exp
    togo2 = y - p2.exp

    if rot % 4 is 0:
        r += 1
        print("")
        slow_print(f'ROUND {r}! FIGHT!')
        slow_print(f"{p1.name}: (lvl {p1.lvl}, exp {p1.exp}). {togo1}exp to next lvl!")
        slow_print(f"{p2.name}: (lvl {p2.lvl}, exp {p2.exp}). {togo2}exp to next lvl!")
        return r
    else:
        return r


def check_state(player1, player2):
    if check_play(player1, player2) is False:
        return False
    else:
        return True


def momentum(player, p_e):
    if player.exp >= p_e:
        return True
    else:
        return False


def keep_fighting():
    while True:
        a = input("Keep Fighting?!?! ('y' or 'n'): ")
        print("")
        if a == 'y':
            return True
        elif a == 'n':
            print('Goodbye!')
            return False
        else:
            print('Please Choose "y" or "n"!')
            continue


def play(x, y):
    if check_state(x, y) is False:
        kf = keep_fighting()
        if kf is not True:
            return False
        if kf is True:
            x.health = 100
            y.health = 100
            slow_print('ITS NOT OVER!!!')
            return True
    else:
        return True


def main():
    funk = Player(name="FunkFoo", health=100, atk=0, exp=0, lvl=0)
    foo = Player(name="FuuBar", health=100, atk=0, exp=0, lvl=0)

    funk_l = round(funk.exp + (funk.exp * .5))
    foo_l = round(foo.exp + (foo.exp * .5))

    round_count = 1
    rotation_count = 0
    slow_print(f'ROUND {round_count}! FIGHT!')
    slow_print(f"{funk.name}:lvl {funk.lvl}, exp {funk.exp}")
    slow_print(f"{foo.name}:lvl {foo.lvl}, exp {foo.exp}")
    while True:
        if get_winner(funk, foo) is True:
            play(funk, foo)
        funk.atk = get_str(funk)
        foo.atk = get_str(foo)
        rotation_count += 1
        round_count = get_round(funk_l, funk, foo_l, foo, round_count, rotation_count)

        experience = swing(funk, foo)

        if experience == funk.name:
            funk.exp += 3
            if momentum(funk, funk_l) is True:
                funk.lvl += 1
            else:
                continue

        if experience != funk.name:
            foo.exp += 3
            if momentum(foo, foo_l) is True:
                foo.lvl += 1
            else:
                continue
        else:
            continue

        play(funk, foo)

        funk_l = funk.exp + (funk.exp * .5)
        foo_l = foo.exp + (foo.exp * .5)

    return


if __name__ == '__main__':
    main()
