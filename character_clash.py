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
"o-" : [3, 20, 3, 2]}
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

    def walk(self, pos):
        pass

    def move(self, players):
        if self.blocking == False:
            self.pos[1] -= 1
            self.blocking = True
        elif self.blocking == True:
            self.pos[1] += 1
            self.blocking = False

        # self.blocking = False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if __name__ == "main":
    main()
main()
