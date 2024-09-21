import os
import datetime
from file_manager import FileManager
from network_manager import NetworkManager

class Shell:
    def __init__(self):
        self.file_manager = FileManager()
        self.network_manager = NetworkManager()

    def display_date(self): 
        print(datetime.datetime.now().strftime("%d-%b-%Y").lower())

    def display_time(self):
        print(datetime.datetime.now().strftime("%H:%M:%S"))

# Method called to display hours, minutes or seconds in unit parameter

    def display_time_units(self, unit):
        now = datetime.datetime.now()
        if unit == 'hours':
            print(now.strftime("%H"))
        elif unit == 'mins':
            print(now.strftime("%M"))
        elif unit == 'secs':
            print(now.strftime("%S"))
        else:
            print("Invalid time unit.")

    def present_working_directory(self):
        return os.getcwd()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

# Starting the shell command loop and not stopped till exited

    def run(self):

        while True:
            command = input("pythonshell> ").strip().split()
            if not command:
                continue

            cmd = command[0]
            try:
                if cmd == "list":
                    print("\n".join(self.file_manager.list_files()))
                elif cmd == "dirs":
                    print("\n".join(self.file_manager.list_dirs()))
                elif cmd == "date":
                    self.display_date()
                elif cmd == "time":
                    if len(command) == 1:
                        self.display_time()
                    elif len(command) == 2:
                        self.display_time_units(command[1].lstrip('-'))
                    else:
                        print("Invalid command.")
                elif cmd == "cat":
                    print(self.file_manager.cat_file(command[1]))
                elif cmd == "head":
                    if len(command) == 3 and command[1] == "-5":
                        print(self.file_manager.head_file(command[2]))
                    else:
                        print("Invalid command.")
                elif cmd == "tail":
                    if len(command) == 3 and command[1] == "-5":
                        print(self.file_manager.tail_file(command[2]))
                    else:
                        print("Invalid command.")
                elif cmd == "copy_file":
                    print(self.file_manager.copy_file(command[1], command[2]))
                elif cmd == "remove_file":
                    print(self.file_manager.remove_file(command[1]))
                elif cmd == "empty_file":
                    print(self.file_manager.empty_file(command[1]))
                elif cmd == "ipconfig":
                    print(self.network_manager.get_ip_address())
                elif cmd == "pwd":
                    print(self.present_working_directory())
                elif cmd == "clear":
                    self.clear_screen()
                elif cmd == "exit":
                    print("Shell exited.")
                    break
                else:
                    print("Invalid command.")
            except IndexError:
                print("Not enough arguments provided.")
            except Exception as e:
                print(f"Error: {e}")
