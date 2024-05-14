import os
import random
import time

green = "\033[32m"
yellow = "\033[33m"
blue = "\033[36m"
normal = "\033[0m"

print(yellow, "\n\n\ncreating BINGO for your Nan 😏👍")
print("\nPlease wait...")
time.sleep(2)
os.system("clear")

box1 = random.randrange(0, 10)
box2 = random.randrange(11, 20)
box3 = random.randrange(21, 30)
box4 = random.randrange(31, 40)
box5 = "BINGO"
box6 = random.randrange(41, 50)
box7 = random.randrange(51, 60)
box8 = random.randrange(61, 80)
box9 = random.randrange(81, 90)

game_bingo = [[box1, box2, box3], [box4, box5, box6], [box7, box8, box9]]

print(blue, "\n\nNikhil's Nan's bingo card Generator.")
print("----------------------------------------")
print()
print(f"""{green}
          {game_bingo[0][0]}  |  {game_bingo[0][1]}   |  {game_bingo[0][2]}
        --------------------- 
          {game_bingo[1][0]} | {game_bingo[1][1]} |  {game_bingo[1][2]}
        ---------------------
          {game_bingo[2][0]} |  {game_bingo[2][1]}   |  {game_bingo[2][2]}
{normal}""")
print()
print()
