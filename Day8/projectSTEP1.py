#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
##Todo-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #Todo-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by 
    # the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#Todo-3: Call the encrypt function and pass in the user inputs. You should be able to test the co
def encrypt(plain_text,amount_shift):
    Caesar_Cipher=""
    for letter in plain_text:
    #for h in hello
        possition=alphabet.index(letter)
        #a[a,b,..].index(h)
        #possition=7
        new_possition=possition+amount_shift
        #new_possition=7+3=10
        new_letter=alphabet[new_possition]
        #new_letter=k
        Caesar_Cipher+=new_letter
    print(Caesar_Cipher)


encrypt(plain_text=text,amount_shift=shift)





    