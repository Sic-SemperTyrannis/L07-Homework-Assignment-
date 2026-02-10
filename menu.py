class Menu:
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
                return int(userInput)
            elif userInput == 'Q' or userInput == '4':
                exit()

    