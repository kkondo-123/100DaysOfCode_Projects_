"""
Name: Kana Kondo
Date: 2025/06/20
Course: 100 Days of Code Day 8
Description: Caesar Cipher
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):
    # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #  by the shift amount and print the decrypted text.

    cipher_text = ""
    abs_shifted = 0
    multiplier = 0
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount

        # If shifted_position < (-1 * len(alphabet)), then error
        """ For instance, if shift was a large number such as 100, shifted_position is smaller
        than -24 (index 0).  
        => Need to research how negative sign plays into modulo calculations
        (Angela used similar code to encrypt function)
        """
        abs_shifted = abs(shifted_position)
        abs_shifted %= len(alphabet)

        if shifted_position > 0:  # positive number
            multiplier = 1
        else:  # If 0 or negative number
            multiplier = -1

        shifted_position = multiplier * abs_shifted
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_text, shift_amount, direction_crypt):
    shift = shift_amount
    if direction_crypt == "decode":
        shift *= -1

    abs_shifted = 0
    multiplier = 0
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift

        abs_shifted = abs(shifted_position)
        abs_shifted %= len(alphabet)

        if shifted_position > 0:  # positive number
            multiplier = 1
        else:  # If 0 or negative number
            multiplier = -1

        shifted_position = multiplier * abs_shifted
        cipher_text += alphabet[shifted_position]

    print(f"Here is the {direction_crypt} result: {cipher_text}")


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


# encrypt(original_text=text, shift_amount=shift)

caesar(original_text=text, shift_amount=shift, direction_crypt = direction)
