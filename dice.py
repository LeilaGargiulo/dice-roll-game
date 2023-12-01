import random
# Initialise player scores to 0
player1_score = 0
player2_score = 0
while player1_score < 20 and player2_score < 20:
    input("Press enter to roll the dice for Player 1:")
    player1_value = random.randint(1, 6)
    print("Player 1 rolled: ", player1_value)
    player1_score += player1_value
    input("Press enter to roll the dice for Player 2:")
    player2_value = random.randint(1, 6)
    print("Player 2 rolled: ", player2_value)
    player2_score += player2_value
print("Game Over")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)




