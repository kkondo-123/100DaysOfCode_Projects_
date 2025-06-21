"""
Name: Kana Kondo
Date: 2025/06/20
Course: 100 Days of Code Day 8
Description: Caesar Cipher
"""

# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:

        # TODO-2: What happens if the user enters a number/symbol/space?
        if letter not in alphabet:  # If the character not an alphabetical character
            # output_text += alphabet   # Mistake: NOT alphabet, but letter
            output_text += letter

        else:
            if encode_or_decode == "decode":
                shift_amount *= -1

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
program_running = True
prompt_user = ''

while program_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    prompt_user = input("Do you want to continue? Type 'E' to exit: ").lower
    if prompt_user == 'e':
        print("Exiting game...")
    else:
        print("Continuing program...\n\n")

print("Thank you and see you again! ")
