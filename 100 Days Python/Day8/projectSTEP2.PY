alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,amount_shift):
    cipher_text=""
    for letter in plain_text:
    #for h in hello
        possition=alphabet.index(letter)
        #a[a,b,..].index(h)
        #possition=7
        new_possition=possition+amount_shift
        #new_possition=7+3=10
        new_letter=alphabet[new_possition]
        #new_letter=k
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text,amount_shift):
    new_cipher_text=""
    for letter in cipher_text:
    #for k in khoor
        possition=alphabet.index(letter)
        #position=alphabet.index(k)=10
        new_possition=possition-amount_shift
        #new_position=10-3=7
        new_letter=alphabet[new_possition]
        new_cipher_text+=new_letter
    print(f"The encoded text is {new_cipher_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

if direction == "encode":
  encrypt(plain_text=text, amount_shift=shift)
elif direction == "decode":
  decrypt(cipher_text=text, amount_shift=shift)
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


