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


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

    location = 0
    new_text = ""

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.
    for chr in original_text:
        # print(f"chr = {chr}")

        # Find letter in alphabet
        location = alphabet.index(chr)
        # print(f"Bef Shift: {location}")

        # Change by shift_amount
        location += shift_amount
        # print(f"Aft Shift: {location}")

        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        location %= len(alphabet)
        # My mistake: 23 instead of 24 because last index is 23

        # Replace letter with alphabet at location in new_text
        new_text += alphabet[location]
        # print(f"new_text = {new_text}")

    # print(f"new_text = {new_text}")

    # # Assign original_text to new_text
    # original_text = new_text
    # print(f"original_text = {original_text}")

    return new_text


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# encrypt(text, shift)
# print(text)
encrypted_msg = encrypt(text, shift)
print(encrypted_msg)