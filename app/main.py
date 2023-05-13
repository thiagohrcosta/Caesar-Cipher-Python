import alphabet
from art import logo

user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.letters.index(letter)
    new_position = position + shift_amount
    end_text += alphabet.letters[new_position]
  print(f"Here's the {user_choice}d result: {end_text}")

should_end = False

while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
