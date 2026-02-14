import os

class Menu():
    def __init__(self):
        self.options = []

    def addOption(self, option):
        self.options.append(option)
    
    def displayMenu(self):
        for index, element in enumerate(self.options): 
            print(f"{index+1} {element}")

    def getInput(self):
        while True:
            self.displayMenu()
            userInput = input().upper() 
            if userInput == '1' or userInput == '2' or userInput == '3' :
                run_bash_cmd(int(userInput))
            elif userInput == 'Q' or userInput == '4':
                exit()
            else:
                print("Invaild input")

def run_bash_cmd(choice):
    print('-' * 80)
    print('You entered #', choice)

    commands = {
        1: 'free -tmh',
        2: r"netstat -an | grep -i Estab | cut -d ':' -f 2,3 | gawk '{print $2}' | grep [0-9] | uniq",
        3: r'df -h | grep "Filesystem\|root"'
    }

    messages = {
        1: 'The available memory is:',
        2: 'The current network connections include:',
        3: 'Available file space is:'
    }

    print(messages[choice])
    os.system(commands[choice])
