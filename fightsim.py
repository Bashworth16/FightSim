import random


def read_lvl():
    return


class Player:
    def __init__(self, name, health, atk, exp, lvl):
        self.name = name
        self.health = health
        self.atk = atk
        self.exp = exp
        self.lvl = lvl


def attack(p1a, p2h):
    p2h = p2h - p1a
    return p2h


def check_die(player):
    if player < 0 or player == 0:
        return True
    else:
        return False


def check_play(player1, player2):
    if check_die(player1.health) is True:
        return False
    if check_die(player2.health) is True:
        return False
    else:
        return True


def coin_flip():
    toss = random.randint(0, 9)
    if toss >= 5:
        return True
    if toss <= 4:
        return False


def block():
    chance = ['Hit', 'Block']
    luck = random.randint(0, (len(chance)))
    if luck is 0:
        return False
    if luck is 1:
        return True


def get_str(player):
    if player.lvl is 0:
        return random.randint(1, 4)
    if 4 > player.lvl > 0:
        return random.randint(3, 6)
    if 7 > player.lvl > 3:
        return random.randint(5, 8)
    if 10 > player.lvl > 6:
        return random.randint(7, 10)
    if 13 > player.lvl > 9:
        return random.randint(9, 12)
    if 16 > player.lvl > 12:
        return random.randint(11, 14)
    if 19 > player.lvl > 15:
        return random.randint(13, 16)
    if 22 > player.lvl > 18:
        return random.randint(15, 18)
    if 25 > player.lvl > 21:
        return random.randint(17, 20)
    if 28 > player.lvl > 24:
        return random.randint(19, 22)
    if 31 > player.lvl > 27:
        return random.randint(25, 101)
