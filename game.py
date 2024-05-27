# import random

# # Define the Snakes and Ladders board
# snakes_ladders = {
#     16: 6,
#     47: 26,
#     49: 11,
#     56: 53,
#     62: 19,
#     64: 60,
#     87: 24,
#     93: 73,
#     95: 75,
#     98: 78
# }

# # Function to get the current position of the player after dice roll
# def dice_roll(player, current_position):
#     input(f"{player}'s turn. Press Enter to roll the dice...")
#     dice_result = random.randint(1, 6)
#     new_position = current_position + dice_result
#     print(f"You rolled a {dice_result}. Moving to position {new_position}")
#     return new_position

# # Function to check for snakes and ladders
# def snake_ladder(position):
#     if position in snakes_ladders:
#         if position < snakes_ladders[position]:
#             print(f"Yikes! You landed on a snake. Sliding down to position {snakes_ladders[position]}!")
#         else:
#             print(f"Great! You climbed a ladder. Moving up to position {snakes_ladders[position]}!")
#         return snakes_ladders[position]
#     return position

# # Function to play the game
# def play():
#     print("Welcome to Snake and Ladder Game.")
#     print("Rules:")
#     print("1. Initially all the players are at starting position i.e. 0.")
#     print("2. Take it in turns to roll the dice.")
#     print("3. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
#     print("4. If you land on the head of a snake, you must slide down to the bottom of the snake.")
#     print("5. The first player to get to the FINAL position is the winner.")
#     print("6. Hit enter to roll the dice.")

#     num_players = int(input("Enter the number of players (1-2): "))
#     if num_players < 1 or num_players > 2:
#         print("Invalid number of players. Please enter a number between 1 and 2.")
#         return
    
#     players = []
#     for i in range(1, num_players + 1):
#         name = input(f"Enter name for Player {i}: ")
#         players.append(name)

#     current_positions = [0] * num_players

#     final_position = 100
#     winner = None

#     while not winner:
#         for i in range(num_players):
#             current_position = current_positions[i]
#             current_position = dice_roll(players[i], current_position)
#             current_position = snake_ladder(current_position)
#             if current_position == final_position:
#                 winner = players[i]
#                 break
#             current_positions[i] = current_position

#     print(f"Congratulations {winner}! You won the game.")

# # Run the game
# play()


import random
# Define the board with ladder positions
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
# Define the snakes positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
def dice_roll():
    return random.randint(1, 6)
def get_position(player, current_position):
    # Check if player lands on a ladder
    if current_position in ladders:
        new_position = ladders[current_position]
        print(f"Player {player} climbed a ladder! Moved to position {new_position}.")
        return new_position
    # Check if player lands on a snake
    elif current_position in snakes:
        new_position = snakes[current_position]
        print(f"Player {player} landed on a snake! Moved to position {new_position}.")
        return new_position
    else:
        return current_position
def play():
    print("Welcome to Snake and Ladder Game.")
    print("Rules:")
    print("1. Initially all the players are at starting position i.e. 0.")
    print("2. Take it in turns to roll the dice.")
    print("3. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
    print("4. If you land on the head of a snake, you must slide down to the bottom of the snake.")
    print("5. The first player to get to the FINAL position is the winner.")
    print("6. Hit enter to roll the dice.")
    player1_position = 0
    player2_position = 0
    
    while True:
        # Player 1's turn
        input("Player 1, press Enter to roll the dice...")
        dice_result = dice_roll()
        player1_position += dice_result
        print(f"Player 1 rolled a {dice_result}.")
        player1_position = get_position(1, player1_position)
        print(f"Player 1 is now at position {player1_position}.\n")
        # Check if Player 1 wins
        if player1_position >= 100:
            print("Player 1 wins!")
            break
        # Player 2's turn
        input("Player 2, press Enter to roll the dice...")
        dice_result = dice_roll()
        player2_position += dice_result
        print(f"Player 2 rolled a {dice_result}.")
        player2_position = get_position(2, player2_position)
        print(f"Player 2 is now at position {player2_position}.\n")
        # Check if Player 2 wins
        if player2_position >= 100:
            print("Player 2 wins!")
            break
play()







