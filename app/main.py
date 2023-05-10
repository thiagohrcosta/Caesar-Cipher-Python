import alphabet

user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")
    