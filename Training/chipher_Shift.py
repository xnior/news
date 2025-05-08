import os
from colorama import Fore, Style
os.system('cls' if os.name == 'nt' else 'clear')



def logo():
    print('''
                     Dev. Eng. Adhemar Júnior
  ___ __ _  ___  ___  __ _ _ __   
 / __/ _` |/ _ \/ __|/ _` | '__|  
| (_| (_| |  __/\__ \ (_| | |     
 \___\__,_|\___||___/\__,_|_|     
                  _               
                 | |              
  ___ _   _ _ __ | |__   ___ _ __ 
 / __| | | | '_ \| '_ \ / _ \ '__|
| (__| |_| | |_) | | | |  __/ |   
 \___|\__, | .__/|_| |_|\___|_|   
       __/ | |                    
      |___/|_|                    ''')


alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
logo()
global historical
historical = ''

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    global historical
    historical = cipher_text
    print(f"The encoded text is: {cipher_text}")
    
    
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    global historical
    historical = plain_text
    print(f"The decoded text is: {plain_text}")
    
    
def caesar(text, shift_amount, direction):
    if direction[0] == "e":
        encrypt(text, shift_amount)
    elif direction[0] == "d":
        decrypt(text, shift_amount)
    else:
        print("Invalid direction. Please type 'encode' or 'decode'.")

should_continue = True

while should_continue:
    os.system('cls' if os.name == 'nt' else 'clear')
    if historical != '':
        print(Fore.CYAN + Style.BRIGHT + "Last Word: " + historical + Style.RESET_ALL)
    logo()
    print(Fore.CYAN + Style.BRIGHT + "\nWelcome to the Caesar Cipher Program!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Choose an option from the menu below:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Encode a message" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Decode a message" + Style.RESET_ALL)
    print(Fore.RED + "3. Exit" + Style.RESET_ALL)

    while True:
        try:
            choice = int(input(Fore.CYAN + "Enter your choice (1/2/3): " + Style.RESET_ALL))
            if choice in [1, 2, 3]:
                break
            else:
                print(Fore.RED + "Invalid choice. Please select 1, 2, or 3." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

    if choice == 1:
        direction = "encode"
    elif choice == 2:
        direction = "decode"
    elif choice == 3:
        should_continue = False
        print(Fore.MAGENTA + "Goodbye!" + Style.RESET_ALL)
        break

    while True:
        try:
            shift = int(input(Fore.CYAN + "Type the shift number: " + Style.RESET_ALL)) % 26
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

    text = input(Fore.CYAN + "Type your message: " + Style.RESET_ALL).lower()
    caesar(text, shift, direction)

    result = input(Fore.YELLOW + "Type 'yes' if you want to go again. Otherwise type 'no': " + Style.RESET_ALL).lower()
    if result[0] == "n":
        should_continue = False
        print(Fore.MAGENTA + "Goodbye!" + Style.RESET_ALL)
    elif result[0] == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(Fore.RED + "Invalid input. Please type 'yes' or 'no'." + Style.RESET_ALL)