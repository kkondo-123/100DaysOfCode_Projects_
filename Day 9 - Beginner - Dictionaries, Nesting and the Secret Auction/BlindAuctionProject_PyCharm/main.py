"""
Name: Kana Kondo
Date: 2025-06-28-Sat
Course: 100 Days of Code Day 9
Description: Blind Auction Project
"""
# import os
from art import logo

print(logo)

bidders = 'y'
name = ''
bid = 0
auction_records = {}
person_num = 1

while bidders == 'y':

    print(f"\n\nBidder #{person_num} shall start bidding...")

    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    auction_records[name] = bid

    # TODO-3: Whether if new bids need to be added
    bidders = input("Are there any other bidders? \nType 'y' for yes: ")

    person_num += 1

    # # Clearing the Screen: https://www.geeksforgeeks.org/clear-screen-python/
    # os.system('cls')

    print("\n" * 20)  # Scroll to next person

# TODO-4: Compare bids in dictionary
highest_bid = bid
winner = ''
for bidder, price in auction_records.items():
    if price >= highest_bid:
        winner = bidder
        highest_bid = price
print(f"The winner is {winner} with a bid of ${highest_bid}")
# Angela used a function to compare bids
