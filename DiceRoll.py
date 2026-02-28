#DiceRoll.py
#Name:Zane Serhan
#Date:2/28/2026
#Assignment:Lab6 DiceRoll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    total = dice1 + dice2
    rolls[total-2] = rolls[total-2]+1
  #print statictics for dice rolls
  dice = 2
  total_rolls = 10000
  for count in rolls:
    percentage = (count/total_rolls)*100
    print(dice, ":", count, "(", round(percentage, 2), "%)")
    dice = dice + 1
if __name__ == '__main__':
  main()
