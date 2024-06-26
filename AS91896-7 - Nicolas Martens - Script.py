from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import os

def fileAccess(mode, row):
    

def createItem(firstRow):
    print("You've chosen to log a rented item. Please enter the below details.")
    firstName = str(input("First Name of customer: "))
    lastName = str(input("Customer's Surname: "))
    rentedItem = str(input("Item that has been rented: "))
    numberItems = int(input("How many items have been rented: "))
    firstName = firstName.title().replace(" ","")
    lastName = lastName.title().replace(" ","")
    rentedItem = rentedItem.title()
    fileAccess("a",firstRow[-1])
    return

def listItems(firstRow):
    print("List")
    return

def deleteItem(firstRow):
    print("Delete")
    return

def editItem(firstRow):
    print("Edit")
    return

def quitProgram():
    print("Quit")
    return

def main():
    dataFile = open("AS91897DATA.txt","a")
    dataFile.close()
    if os.path.exists("AS91897ROW.txt") == False:
        rowFile = open("AS91897ROW.txt","a")
        rowFile.write("0")
        rowFile.close()
    commands = ["CreateItem", "C", "ListItems", "L", "DeleteItem", "D", "EditItem", "E", "QuitProgram", "Q"]
    print("Runnable Commands: (Not case or whitespace sensitive)")
    print(f"{commands[0]}\t({commands[1]})\t|\tAllows you to log a new item that has been rented.")
    print(f"{commands[2]}\t({commands[3]})\t|\tAllows you to list all currently rented items.")
    print(f"{commands[4]}\t({commands[5]})\t|\tAllows you to log an item that has been returned.")
    print(f"{commands[6]}\t({commands[7]})\t|\tAllows you to edit the details of a rented item.")
    print(f"{commands[8]}\t({commands[9]})\t|\tQuits the program.")
    for i in range(10):
        commands[i] = commands[i].lower()
    while 1:
        rowFile = open("AS91897ROW.txt","r")
        firstRow = rowFile.readline().split()
        rowFile.close()
        action = input("\nEnter Command: ")
        action = action.lower().replace(" ","")
        match action:
            case action if action in [commands[0], commands[1]]:
                createItem(firstRow)
            case action if action in [commands[2], commands[3]]:
                listItems(firstRow)
            case action if action in [commands[4], commands[5]]:
                deleteItem(firstRow)
            case action if action in [commands[6], commands[7]]:
                editItem(firstRow)
            case action if action in [commands[8], commands[9]]:
                quitProgram()
                break
            case _:
                print("\nError, Command Entered is Invalid")
                continue

if __name__ == "__main__":
    main()
