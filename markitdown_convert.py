import sys
import os
import datetime
import re
from colorama import Fore, Style
from markitdown import MarkItDown

def display_converter_header(developer_name):
    """Displays a beautiful header for the PDF to Markdown converter."""
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + f" ✨ Welcome to the Elegant File Converter! ✨" + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + f" 👨‍💻 Developed by: {developer_name} 👨‍💻" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)
    print()

def get_date_input(prompt):
    """Gets a date input from the user with validation."""
    date_pattern = re.compile(r"^\d{2}-\d{2}-\d{4}$")
    while True:
        date_str = input(Fore.LIGHTYELLOW_EX + prompt + Style.RESET_ALL).strip()
        if not date_str:
            return datetime.datetime.now().strftime("%d-%m-%Y")
        if date_pattern.match(date_str):
            return date_str
        print(Fore.RED + Style.BRIGHT + "Invalid date format. Please use DD-MM-YYYY." + Style.RESET_ALL)

def get_file_type():
    """Prompts the user to select a file type."""
    file_types = {".pdf", ".doc", ".xlsx", ".ppt"}
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 📂 Select the file type to process: 📂" + Style.RESET_ALL)
    for key, value in enumerate(file_types):
        print(f"{Fore.WHITE}{key + 1}: {value}{Style.RESET_ALL}")

    while True:
        choice_str = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Enter the number corresponding to the file type: " + Style.RESET_ALL).strip()
        try:
            choice = int(choice_str)
            file_types_list = list(file_types)
            if 1 <= choice <= len(file_types_list):
                return file_types_list[choice - 1]
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid selection. Please choose a number from the list." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter a valid number." + Style.RESET_ALL)

def find_files_by_date(folder, extension, start, end):
    """Finds files with the specified extension within the given date range."""
    found_files = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(extension.lower()):
            filepath = os.path.join(folder, filename)
            try:
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                start_date_obj = datetime.datetime.strptime(start, "%d-%m-%Y")
                end_date_obj = datetime.datetime.strptime(end, "%d-%m-%Y") + datetime.timedelta(hours=23, minutes=59, seconds=59)
                if start_date_obj <= mod_time <= end_date_obj:
                    found_files.append(filename)
            except Exception as e:
                print(Fore.YELLOW + f"Warning: Could not process timestamp for '{filename}'. {e}" + Style.RESET_ALL)
    return found_files

def select_file_to_process(file_list):
    """Allows the user to select a file from a list."""
    if not file_list:
        print(Fore.YELLOW + Style.BRIGHT + "No files found matching your criteria." + Style.RESET_ALL)
        input(Fore.YELLOW + Style.BRIGHT + "Press Enter to exit." + Style.RESET_ALL)
        return None

    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f" 📄 Found {len(file_list)} files: 📄" + Style.RESET_ALL)
    for idx, file in enumerate(file_list, start=1):
        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, file)))
        print(f"{Fore.WHITE}{idx}: {file} - Modified: {mod_time.strftime('%d-%m-%Y %H:%M:%S')}{Style.RESET_ALL}")

    while True:
        choice_str = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "Enter the number of the file to open (or 0 to process all) or x to exit: " + Style.RESET_ALL).strip()
        if choice_str[0].lower() == 'x':
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 👋 Exiting the file selection. 👋" + Style.RESET_ALL)
            return None, None
        try:
            choice = int(choice_str)
            if choice == 0:
                return file_list, None
            elif 1 <= choice <= len(file_list):
                return [file_list[choice - 1]], file_list[choice - 1]
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid selection." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter a number." + Style.RESET_ALL)

def process_file(filepath):
    """Converts the given file to Markdown and prints the output."""
    try:
        md = MarkItDown()
        markdown_output = md.convert(filepath)
        print(Fore.GREEN + Style.BRIGHT + "\n 📜 Conversion Output: 📜" + Style.RESET_ALL)
        print(markdown_output)
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + " ✅ Conversion completed successfully. ✅" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f" ❌ Error during conversion of '{os.path.basename(filepath)}': {e} ❌" + Style.RESET_ALL)

def ask_to_process_another(backup_list):
    """Asks the user if they want to process another file."""
    while True:
        another = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "Do you want to process another file? (yes/no): " + Style.RESET_ALL).strip().lower()
        if another in ['yes', 'y']:
            return True, backup_list
        elif another in ['no', 'n']:
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 👋 Exiting the program. Goodbye! 👋" + Style.RESET_ALL)
            return False, None
        else:
            print(Fore.YELLOW + Style.BRIGHT + "Invalid input. Please type 'yes' or 'no'." + Style.RESET_ALL)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    developer_name = "Dev. Eng. Adhemar Junior"
    display_converter_header(developer_name)

    folder_path = "C:\\Users\\Adhemar Jr\\Downloads"  # You might want to make this configurable
    start_date_str = get_date_input("Enter the start date (DD-MM-YYYY) or press Enter for today: ")
    end_date_str = get_date_input("Enter the end date (DD-MM-YYYY) or press Enter for today: ")
   

    selected_extension = get_file_type()
    found_files = find_files_by_date(folder_path, selected_extension, start_date_str, end_date_str)
    all_found_files = list(found_files) # Create a backup

    while True:
        files_to_process, selected_single_file = select_file_to_process(found_files)

        if not files_to_process:
            break

        if selected_single_file:
            process_file(os.path.join(folder_path, selected_single_file))
            found_files.remove(selected_single_file) # Remove processed file from the list
        elif files_to_process:
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\n 🚀 Processing all selected files: 🚀" + Style.RESET_ALL)
            for file in list(files_to_process): # Iterate over a copy to allow removal
                process_file(os.path.join(folder_path, file))
                if file in found_files:
                    found_files.remove(file)

        continue_processing, backup_list = ask_to_process_another(all_found_files)
        if not continue_processing:
            break
        elif backup_list:
            found_files = list(backup_list) # Restore the original list for the next iteration