import os, random
os.system('cls' if os.name == 'nt' else 'clear')
from colorama import Fore, Style


words = ["hello", "world", "python", "programming"]

correct_words = []
place_holder=""
game_over = False
lives = 7

selected_word = random.choice(words)
word_length = len(selected_word)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '''Bem vindo ao sistema de Jogo da forca
                                Developed by Eng. Adhemar Jr
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                                
                                ''')                            
draw = ['''
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \\
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / 
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |      (_)
        |      \|/
        |       
        |      
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |      (_)
        |      \|
        |  
        |  
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |      (_)
        |       |
        |  
        |  
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |      (_)
        |  
        |  
        |  
        |
    ____|___
        
        ''','''
         _______
        |/      |
        |  
        |  
        |  
        |  
        |
    ____|___
        
        ''']

print(draw[lives])

for position in range(word_length):
    place_holder += "_"
print(place_holder)

while not game_over:
    guess = input('Insira a letra que poderia se encaixar no local "_": ')
    
    display = ""
    for letter in selected_word:
        if guess == letter:
            display += letter
            correct_words.append(guess)
        elif letter in correct_words:
            display += letter
        else:
            display += "_"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    if guess not in selected_word:
        lives -= 1
        if lives == 0:
            print(Fore.RED + Style.BRIGHT + "Você Perdeu!" + Style.RESET_ALL)
            print(f"A palvra correta era --> '{selected_word}' ")
            game_over = True
    print(f"Tentativas: {lives} ")
        
    print(draw[lives])
            
    print(display)
    
    if selected_word == display:
        print("Acertou todas as letras")
        break
    