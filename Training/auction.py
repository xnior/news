import os
from colorama import Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bid_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        bid_amount = int(bid_dictionary[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(Fore.GREEN + Style.BRIGHT + f"The winner is {winner} with a bid of {highest_bid}!" + Style.RESET_ALL)
    


def logo():
    print(Fore.MAGENTA + Style.BRIGHT + '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
''' + Style.RESET_ALL)
logo()
print(Fore.CYAN + Style.BRIGHT + "Welcome to the Auction House!" + Style.RESET_ALL)
print(Fore.YELLOW + Style.BRIGHT + "Here you can bid on items and win them!" + Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + "Let's get started!" + Style.RESET_ALL)


bids={}
continue_bidding = True
while continue_bidding:
    name = input("Enter the/your name: ")
    print(Fore.CYAN + Style.BRIGHT + f"Hello {name}, let's start bidding!" + Style.RESET_ALL)
    price = input("Enter your bid value: ")
    print(Fore.YELLOW + Style.BRIGHT + f"Your bid value is {price}!" + Style.RESET_ALL)
    bids[name] = price
    more_bids = input("Do you want to add more bids? (yes/no): ").lower()
    try:
        if more_bids[0] == 'n':
            continue_bidding = False
            find_highest_bidder(bids)
    except IndexError:
        print(Fore.RED + "Please enter a valid response." + Style.RESET_ALL)