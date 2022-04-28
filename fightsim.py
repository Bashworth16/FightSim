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
