from markitdown import MarkItDown
import os, sys
from colorama import Fore, Style

def main(args):
    os.system('cls' if os.name == 'nt' else 'clear')

    def display_converter_header():
        """Displays the header of the converter with developer information."""
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + " 📜 MarkItDown Converter 📜" + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + " Developed by: Eng. Adhemar Jr" + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + " ----------------------------------------" + Style.RESET_ALL)
        
        
    display_converter_header()    
    md = MarkItDown()

    markdownoutput = md.convert(args)
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + " ----------------------------------------" + Style.RESET_ALL)
    print(markdownoutput)
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + " ----------------------------------------" + Style.RESET_ALL)
        
    input("Press Enter to Exit...")
input_args = sys.argv[1]
main(input_args)