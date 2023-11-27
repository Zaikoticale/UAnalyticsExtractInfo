import pyfiglet
name = pyfiglet.figlet_format("Analytics Backup", font="small")
by = pyfiglet.figlet_format("by Zaikoticale")

class ConsoleView:
    def display_succes(self):
        print("\033[1m\033[91m")
        print(name)
        print(by)
        print("\033[92m")
        print("Success!")
        print("The report was saved in the backup folder.")
        print("\033[92m\033[1mDone!\033[0m")

    def display_error(self, error):
        print(f"Error: {error}")
