"""
Name: Kana Kondo
Date: 2025-06-28-Sat
Course: 100 Days of Code Day 11
Description: Blackjack
"""


"""
Chose your difficulty
Normal 😎: Use all Hints below to complete the project.
Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Expert 🤯: Only use Hint 1 to complete the project.
Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.

"""

import random
from art import logo

# TODO: Hint 1
# Go to this website and try out the Blackjack game:
# https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
# https://appbrewery.github.io/python-day11-demo/

# TODO: Hint 2
# Read this breakdown of program requirements:
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# TODO: Hint 3
# Download and read this flow chart I've created:
# https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# TODO: Hint 4
# Create a deal_card() function that uses the List below to return a random card.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Remember that 11 is the Ace.
def deal_card():
    return random.choice(cards)
    # https://www.geeksforgeeks.org/python/python-select-random-value-from-a-list/

# TODO: Hint 6
# Create a function called calculate_score() that takes a List of cards as input and returns the sum of all the cards in the List as the score. Google the sum() function to help you do this.
def calculate_score(cards):
    score = sum(cards)

    # TODO: Hint 7
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if score == 21 and len(cards) == 2:
        score = 0

    # TODO: Hint 8
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to Google to find the documentation on the Python built-in functions append() and remove().
    # https://developers.google.com/edu/python/lists#list-methods
    elif score > 21 and 11 in cards:
        index = cards.index(11)
        cards[index] = 1

        # Re-evaluate score
        score = sum(cards)

    return score

def continue_key():
    input("\n\nPress any key to continue...")


# TODO: Hint 13
# Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
def compare(user, computer):
    print("\n\n-------------------Results-------------------")
    continue_key()

    if user == computer:
        print(f"You and the computer both have the same score of {user}. It's a draw.")
    elif computer == 0:
        print(f"Computer has a blackjack. You lose. ")
    elif user == 0:
        print(f"You have a blackjack. You win! ")
    elif user > 21:
        print(f"Your score is {user}. You went over. You lose. ")
    elif computer > 21:
        print(f"Computer score is {computer} and went over. Computer loses. ")
    else:
        if user > computer:
            print(f"User had a higher score of {user} over {computer}. You win! ")
        else:
            print(f"Computer had a higher score of {computer} over {user}. Computer wins.  ")


def reveal_cards(user_c, comp_c, user_s, comp_s):
    print("\n\n-------------------Showdown-------------------")
    continue_key()

    print(f"User: Hand {user_c},\t Score {user_s}")
    print(f"Computer: Hand {comp_c},\t Score {comp_s}")

restart_game = 'y'

while restart_game == 'y':
    print(logo)

    # TODO: Hint 5
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_continue = True
    user_score = -1
    computer_score = -1

    # TODO: Hint 11
    # The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while game_continue:

        print(f"user_cards = {user_cards}")
        # print(f"computer_cards = {computer_cards}")

        # TODO: Hint 9
        # Call the function calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # scores = [user_score, computer_score]

        print(f"user_score = {user_score}")
        # print(f"computer_score = {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            game_continue = False
        else:
            # TODO: Hint 10
            # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

            user_draw_card = input("\n\nDo you want to draw another card? \nType 'y' for yes, any other key for no: ")
            if user_draw_card == 'y':
                user_cards.append(deal_card())
            else:
                game_continue = False

    print("\nUser turn ended...")

    # continue_key()

    # print("Computer turn starts...")
    # TODO: Hint 12
    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score < 17:
        # print("Added card...")
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # print("Computer turn ended...")

    reveal_cards(user_cards, computer_cards, user_score, computer_score)

    compare(user_score, computer_score)

    # TODO: Hint 14
    # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    restart_game = input("\n\nDo you want to restart the game? \nType 'y' for yes and any other key to exit: ")
    if restart_game == 'y':
        print("\n" * 30)

print("Bye Bye! ")




#
# import random
# from art import logo
#
# print(logo)
#
# # TODO: Hint 1
# # Go to this website and try out the Blackjack game:
# # https://games.washingtonpost.com/games/blackjack/
# # Then try out the completed Blackjack project here:
# # https://appbrewery.github.io/python-day11-demo/
#
# # TODO: Hint 2
# # Read this breakdown of program requirements:
# # http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# # Then try to create your own flowchart for the program.
#
# # TODO: Hint 3
# # Download and read this flow chart I've created:
# # https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
#
# # # TODO: Hint 4
# # Create a deal_card() function that uses the List below to return a random card.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # Remember that 11 is the Ace.
#
# def deal_card():
#     return random.choice(cards)
#
# # https://www.geeksforgeeks.org/python/python-select-random-value-from-a-list/
#
# # TODO: Hint 5
# # Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = [deal_card(), deal_card()]
# # user_cards = [11, 11]
# computer_cards = [deal_card(), deal_card()]
#
# # print(f"user_cards = {user_cards}")
# # print(f"computer_cards = {computer_cards}")
#
# # TODO: Hint 6
# # Create a function called calculate_score() that takes a List of cards as input and returns the sum of all the cards in the List as the score. Google the sum() function to help you do this.
# def calculate_score(cards):
#     score = sum(cards)
#
#     # TODO: Hint 7
#     # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#     if score == 21 and len(cards) == 2:
#         score = 0
#
#     # TODO: Hint 8
#     # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to Google to find the documentation on the Python built-in functions append() and remove().
#     # https://developers.google.com/edu/python/lists#list-methods
#     elif score > 21 and 11 in cards:
#         # print("Over 21 and has an ace!")
#         index = cards.index(11)
#         # print(f"index of ace = {index}")
#         cards[index] = 1
#
#         # Re-evaluate score
#         score = sum(cards)
#
#     return score
#
#
# # print(f"sum of user_cards = {calculate_score(user_cards)}")
# # print(f"sum of computer_cards = {calculate_score(computer_cards)}")
#
# game_continue = True
# user_score = -1
# computer_score = -1
#
# # TODO: Hint 11
# # The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
# while game_continue:
#
#     print(f"user_cards = {user_cards}")
#     print(f"computer_cards = {computer_cards}")
#
#     # TODO: Hint 9
#     # Call the function calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     # scores = [user_score, computer_score]
#
#     print(f"user_score = {user_score}")
#     print(f"computer_score = {computer_score}")
#
#     if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
#         game_continue = False
#     else:
#         # TODO: Hint 10
#         # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#
#         user_draw_card = input("\n\nDo you want to draw another card? \nType 'y' for yes, any other key for no: ")
#         if user_draw_card == 'y':
#             user_cards.append(deal_card())
#
#         # draw_another = True
#         # while draw_another:
#         #     user_draw_card = input("\n\nDo you want to draw another card? \nType 'y' for yes, any other key for no: ")
#         #
#         #     if user_draw_card == 'y':
#         #         user_cards.append(deal_card())
#         #     else:
#         #         draw_another = False
#
#
# print("Game ended....")
#
# # TODO: Hint 12
# # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
# while computer_score < 17:
#     computer_cards.append(deal_card())
#
# # TODO: Hint 13
# # Create a function called compare() and pass in the user_score and computer_score.
# # If the computer and user both have the same score, then it's a draw.
# # If the computer has a blackjack (0), then the user loses.
# # If the user has a blackjack (0), then the user wins.
# # If the user_score is over 21, then the user loses.
# # If the computer_score is over 21, then the computer loses.
# # If none of the above, then the player with the highest score wins.
#
# def compare(user, computer):
#     print("\n\n-------------------Showdown-------------------")
#     if user == computer:
#         print(f"You and the computer both have the same score of {user}. It's a draw.")
#     elif computer == 0:
#         print(f"Computer has a blackjack. You lose. ")
#     elif user == 0:
#         print(f"You have a blackjack. You win! ")
#     elif user > 21:
#         print(f"Your score is {user}. You went over. You lose. ")
#     elif computer > 21:
#         print(f"Computer score is {computer} and went over. Computer loses. ")
#     else:
#         if user > computer:
#             print(f"User had a higher score of {user} over {computer}. You win! ")
#         else:
#             print(f"Computer had a higher score of {computer} over {user}. Computer wins.  ")
#
# compare(user_score, computer_score)
#
# # TODO: Hint 14
# # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# restart_game = input("\n\nDo you want to restart the game? \nType 'y' for yes and any other key to exit: ")
# if restart_game == 'y':
#     print("\n" * 30)
# else:
#     print("Bye Bye! ")
