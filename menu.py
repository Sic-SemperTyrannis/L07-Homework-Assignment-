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

def run_bash_cmd(some_choice):
    print('-' * 80, '\n')
    print('You entered #', some_choice)
    if (some_choice == 1):
        print('The available memory is ')
        os.system('free -tmh')
    elif (some_choice == 2):
        print('The current network connections include: ')
        os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
    elif (some_choice == 3):
        print('Available file space is: ')
        os.system('df -h | grep \"Filesystem\|root\"')        
    return    