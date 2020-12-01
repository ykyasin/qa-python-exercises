import dice

first_roll = dice.diceroll()
print("You roll the dice, the first number is: " + str(first_roll))
second_roll = dice.diceroll()
print("You roll it again, the second number is " + str(second_roll) + " with a total of " + str(first_roll + second_roll))