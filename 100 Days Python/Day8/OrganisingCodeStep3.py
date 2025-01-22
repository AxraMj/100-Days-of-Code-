alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,amount_shift):
    cipher_text=""
    for letter in plain_text:
        possition=alphabet.index(letter)
        new_possition=possition+amount_shift
        new_letter=alphabet[new_possition]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,amount_shift):
    new_cipher_text=""
    for letter in cipher_text:
        possition=alphabet.index(letter)
        new_possition=possition-amount_shift
        new_letter=alphabet[new_possition]
        new_cipher_text+=new_letter
    print(f"The encoded text is {new_cipher_text}")

if direction == "encode":
  encrypt(plain_text=text, amount_shift=shift)
elif direction == "decode":
  decrypt(cipher_text=text, amount_shift=shift)


