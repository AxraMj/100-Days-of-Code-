##Todo-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text,amount_shift,cipher_text):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction=="encode":
        cipher_text=""
        for letter in plain_text:
            possition=alphabet.index(letter)
            new_possition=possition+amount_shift
            new_letter=alphabet[new_possition]
            cipher_text+=new_letter
        print(f"The encoded text is {cipher_text}")

    elif direction=="decode":
        new_cipher_text=""
        for letter in cipher_text:
            possition=alphabet.index(letter)
            new_possition=possition-amount_shift
            new_letter=alphabet[new_possition]
            new_cipher_text+=new_letter
        print(f"The encoded text is {new_cipher_text}")
    else:
        print("Please check something is wrong!!")


caesar(plain_text=text,amount_shift=shift,cipher_text=text)




#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.