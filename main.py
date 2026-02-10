from menu import Menu
import os
mainMenu = Menu()

mainMenu.addOption("Check available memory")
mainMenu.addOption("View network connection")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")

userInput = mainMenu.getInput()


#userInput = Menu.getInput()
