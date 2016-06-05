#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random

#==================================================================================================#
#Asks the player what row and column they want to hit
def GetRowColumn():
  print()
  Column = int(input("Please enter column: "))
  Row = int(input("Please enter row: "))
  print()
  return Row, Column
#==================================================================================================#
####################################################################################################


          
def MakePlayerMove(Board, Ships):
  Row, Column = GetRowColumn() #Uses a function to ask what row and column the player wants to hit
  if Board[Row][Column] == "m" or Board[Row][Column] == "h":
    print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
  elif Board[Row][Column] == "-":
    print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
    Board[Row][Column] = "m" #if the point is a miss, it displays this on the board using "m"
  else:
    print("Hit at (" + str(Column) + "," + str(Row) + ").")
    Board[Row][Column] = "h"
#==================================================================================================#
####################################################################################################  


#==================================================================================================#        
def SetUpBoard(): #Creates a 10x10 board filled with dashes
  Board = []
  for Row in range(10): #This will loop and create 10 instances of Row
    BoardRow = [] #Sets BoardRow as being empty
    for Column in range(10): #This will loop create 10 instances of Column
      BoardRow.append("-") #Adds 10 dashes to BoardRow
    Board.append(BoardRow) #Adds BoardRow to Board to create a 2D array (this means there will be 10 lists of 10 dashes)
  return Board
#==================================================================================================#
####################################################################################################


#==================================================================================================#
def LoadGame(Filename, Board):
  BoardFile = open(Filename, "r") #loads board from a text file
  for Row in range(10): #imports the board from the text file into a 2D array
    Line = BoardFile.readline()
    for Column in range(10):
      Board[Row][Column] = Line[Column]
  BoardFile.close()
#==================================================================================================#
####################################################################################################


#==================================================================================================#
def PlaceRandomShips(Board, Ships): #Randomises the place where the ship is placed
  for Ship in Ships: #uses a for loop to run through each ship
    Valid = False
    while not Valid:
      Row = random.randint(0, 9) #decides what row the ship starts in
      Column = random.randint(0, 9) #decides what column the ship starts in
      HorV = random.randint(0, 1) #decides whether the ship is horizontal or vertical
      #################
      if HorV == 0:
        Orientation = "v" 
      else:
        Orientation = "h"
      ################# Assigns a "v" or "h" to Orientation depending on HorV
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation) #uses a function to check if it's a valid position
      #If valid is false then it runs through the while loop to give the ship a new position
      #If valid is true then it just continues
    print("Computer placing the " + Ship[0])
    PlaceShip(Board, Ship, Row, Column, Orientation) #uses a function to put the ship on the board
#==================================================================================================#
####################################################################################################


#==================================================================================================#
def PlaceShip(Board, Ship, Row, Column, Orientation): #actually places the ship on the board
  ################################ Vertical ships
  if Orientation == "v": 
    for Scan in range(Ship[1]):
      Board[Row + Scan][Column] = Ship[0][0] #adds the letter corresponding to the ship to Board in the position
                  #Scan adds onto Row so the letter of the ship moves vertically on the board
  ################################ Horizontal ships
  elif Orientation == "h":
    for Scan in range(Ship[1]):
      Board[Row][Column + Scan] = Ship[0][0] #adds the letter corresponding to the ship to Board in the position
                  #Scan adds onto Row so the letter of the ship moves vertically on the board
#==================================================================================================#
####################################################################################################


#==================================================================================================#
def ValidateBoatPosition(Board, Ship, Row, Column, Orientation): #Checks if the ship's place on the board is valid
  ########################## Makes sure the ship stays on the board when it's placed
  if Orientation == "v" and Row + Ship[1] > 10: #Makes sure the ship does not go off its row
    return False #valid becomes false and it has to run through the while loop in PlaceRandomShips again
  elif Orientation == "h" and Column + Ship[1] > 10: #Makes sure the ship does not go off its column
    return False #valid becomes false and it has to run through the while loop in PlaceRandomShips again
  else:
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-": #If the ship is in the same place as another ship it's not valid
          return False #valid becomes false and it has to run through the while loop in PlaceRandomShips again
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-": #If the ship is in the same place as another ship it's not valid
                                        #any position on the board that's not a dash means there is a ship there
          return False #valid becomes false and it has to run through the while loop in PlaceRandomShips again
  return True
#==================================================================================================#
####################################################################################################



def CheckWin(Board):
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True
#==================================================================================================#
####################################################################################################


 
def PrintBoard(Board):
  print()
  print("The board looks like this: ")  
  print()
  print (" ", end="")
  for Column in range(10):
    print(" " + str(Column) + "  ", end="")
  print()
  for Row in range(10):
    print (str(Row) + " ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print(" ", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print(" ", end="")                
      else:
        print(Board[Row][Column], end="")
      if Column != 9:
        print(" | ", end="")
    print()
#==================================================================================================#
####################################################################################################


#==================================================================================================#       
def DisplayMenu(): #Prints out the menu
  print("MAIN MENU")
  print()
  print("1. Start new game")
  print("2. Load training game")
  print("9. Quit")
  print()
####################################################################################################


#==================================================================================================# 
def GetMainMenuChoice(): #Asks for what option the player wants to choose on the menu
  print("Please enter your choice: ", end="")
  Choice = int(input()) #Accepts user input if it's an integer (if not it displays an error)
  print()
  return Choice
#==================================================================================================#
####################################################################################################


#==================================================================================================#
def PlayGame(Board, Ships):
  GameWon = False
  while not GameWon: #It keeps looping until the game is won i.e. all the ships are completely hit
    PrintBoard(Board) #displays the board
    MakePlayerMove(Board, Ships) #the player picks which point they want to hit
    GameWon = CheckWin(Board) #checks if the player won, and makes GameWon true or false
    if GameWon: #if the player has won, it tells the player that all the ships are sunk
                #and the while loop will end as GameWon is now True
      print("All ships sunk!")
      print()
#==================================================================================================#
####################################################################################################


#==================================================================================================#
if __name__ == "__main__":
  TRAININGGAME = "Training.txt" #the training game text file
  MenuOption = 0
  while not MenuOption == 9: #if the player chooses 9, the while loop stops running (the game stops running)
    Board = SetUpBoard()
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
      #This holds all the ships with its name and size
    DisplayMenu() #Prints out the menu
    MenuOption = GetMainMenuChoice()
    if MenuOption == 1: #generates ships and starts the game
      PlaceRandomShips(Board, Ships) #places ships in random places on the board (creates a board)
      PlayGame(Board,Ships) #plays the game and keeps running until the game is won
                            #when the game is done it loads the menu again and the player can play again
    if MenuOption == 2: #loads training game
      LoadGame(TRAININGGAME, Board) #loads the training board into the Board variable from a text file
      PlayGame(Board, Ships) #plays the game and keeps running until the game is won
#==================================================================================================#
####################################################################################################






      
