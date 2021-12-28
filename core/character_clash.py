import click as clk
import random
from time import sleep
from os import system, name

def main():
    players = []
    players.append(Player([5, 6]))
    game = PlayGrid(players)
    game.update("Up")
#    while len(game.players) < 1:
    sleep(2)
    game.update("Down")
    sleep(2)
    game.update("Up")
    sleep(2)
    game.update("Down")

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
        for row in range(1, 30):
            str = ""
            for i in range(1, 100):
                str += "`"
            self.grid[row] = str

            # Sword # bow # assassin
# Classes = ["o/", "o)", "o-"]
# stats = [speed, damage, range, time]

stats_dict = {"o/" : [2, 25, 2, 3],
"o)" : [2, 35, 3, 4],
"o-" : [3, 20, 1, 2]}
class Player:
    def __init__(self, pos):
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
        if dir == 1:
            self.pos[0] += self.speed
        elif dir == 2:
            self.pos[0] -= self.speed
        elif dir == 3:
            self.pos[1] += self.speed
        self.turns = 1

# Behaviors
    def attack_available(self):
        pass
    def move(self, players):
         self.blocking = False
         self.attacking = False
         selection = 1
         selections = []
         param = ""
         for player in players:
             if player.pos[1] == self.pos[1] and player.pos[0] == self.pos[0]:
                 pass
             else:
                 if attackavailable == True:
                     # walk = 1, block = 2, attack = 3
                     if self.health > 45 and index in attacks_available:
                         if player.attacking == True:
                             selection = 3
                             self.pursuing = index
                         else:
                             if player.health > 35 and self.health < 50:
                                 self.pursuing = player.pos
                                 selection = 2
                 else:
                     selection = random.choice([1, 2, 3])
             selections.append(selection)
         mu = sum(selections) / len(selections)
         selection = int(round(mu))
         if selection == 1:
             if self.pursuing != None:
                 self.pursue()
             else:
                 self.random_walk()
         if selection == 2:
              pass
         if selection == 3:
              pass











def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if __name__ == "main":
    main()
main()
