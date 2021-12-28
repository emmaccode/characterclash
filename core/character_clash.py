import click as clk
import random
from time import sleep
from os import system, name


CHAR_W = 30
CHAR_H = 100

def main():
    players = []
    players.append(Player([11, 20], 0))
    players.append(Player([5, 6], 1))
    players.append(Player([20, 10], 2))
    game = PlayGrid(players)
    for i in range(1, 50):
        sleep(.5)
        game.update("".join(["Iteration: ", str(i)]))

class PlayGrid:
        # Essentials
    def __init__(self, players):
        self.players = players
        self.update("Character Clash Game Started")

    def update(self, message):
        clear()
        self.empty_grid()
        self.draw_players(self.grid)
        self.make_moves()
        print(self.draw_grid())
        print("\n" + message)

    # Player Management
    def draw_players(self, grid):
        for player in self.players:
            modifier = 0
            # True = right, False = left
            if player.facing == True:
                modifier = 1
            else:
                modifer = -1
                # [0] = x, [1] = y
            newpos = player.pos
            current = list(grid[newpos[1]])
            current[newpos[0]] = player.symbol[0]
            current[newpos[0] + modifier] = player.symbol[1]
            current = "".join(current)
            self.grid[newpos[1]] = current

    def make_moves(self):
        [player.move(self.players) for player in self.players]

        # Grid
    def draw_grid(self):
        print_s = "\n"
        for key in self.grid:
            print_s = print_s + self.grid[key] + "\n"
        return(print_s)

    def empty_grid(self):
        self.grid = dict()
        str = ""
        for row in range(1, CHAR_W):
            str = ""
            for i in range(1, CHAR_H):
                str += "`"
            self.grid[row] = str

            # Sword # bow # assassin
# Classes = ["o/", "o)", "o-"]
# stats = [speed, damage, range, time]

stats_dict = {"o/" : [2, 25, 2, 3],
"o)" : [2, 35, 3, 4],
"o-" : [3, 20, 1, 2]}
class Player:
    def __init__(self, pos, id):
        self.id = id
        self.pos = pos
        self.health = 100
        self.blocking = True
        self.attacking = False
        type = random.choice(["o/", "o)", "o-"])
        self.speed = stats_dict[type][0]
        self.damage = stats_dict[type][1]
        self.range = stats_dict[type][2]
        self.time = stats_dict[type][3]
        self.symbol = type
        self.facing = True
        self.attacking = False
        self.pursuing = None
        self.attackavailable = False
        self.attacks_available = []
        self.turns = 0
        # Base
    def random_walk(self):
                # 1 r, 2 l, 3 up, 4, down
        dir = random.choice([1, 2, 3, 4])
        self.walk(dir)

    def walk(self, dir):
        if dir == 1:
            if not self.pos[0] + self.speed >= CHAR_H - 1:
                self.pos[0] += self.speed
                self.facing = True

        elif dir == 2:
            if not self.pos[0] - self.speed <= 2:
                self.pos[0] -= self.speed
                self.facing = False

        elif dir == 3:
            if not self.pos[0] - self.speed <= 2:
                self.pos[1] -= self.speed
        elif dir == 4:
            if not self.pos[0] + self.speed >= CHAR_W - 1:
                self.pos[1] += self.speed
        self.turns += 1

# Behaviors
    def attack_available(self, players):
        for player in players:
            if player.pos[0] != self.pos[0] and self.pos[1] != player.pos[1]:
                if abs(player.pos[0] - self.pos[0]) <= self.range:
                    self.attacks_available.append(player.id)
                elif abs(player.pos[1] - self.pos[1]) <= self.range:
                    self.attacks_available.append(player.id)

    def move(self, players):
         self.attacks_available = []
         self.blocking = False
         self.attacking = False
         self.attack_available(players)
         selection = 1
         selections = [1, 1, 1, 1, 2, 2]
         if len(self.attacks_available) > 0:
             selections.append(3)
         selection = random.choice(selections)
         if selection == 1:
             if self.pursuing != None:
                 self.pursue()
             else:
                 self.random_walk()
         if selection == 2:
              self.blocking = True
              self.turns += 1
         if selection == 3:
             self.attacking = True
             self.call_attack()
    def call_attack(self):
        pass
    def pursue(self):
        pass


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if __name__ == "main":
    main()
main()
