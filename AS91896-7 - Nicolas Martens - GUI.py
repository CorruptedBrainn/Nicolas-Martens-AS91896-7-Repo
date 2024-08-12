from tkinter import Tk as tk
from tkinter import ttk
from tkinter import messagebox as mb
import os
import re

root = tk()
root.title("Julie's Party Hire Store")
mainFrame = ttk.Frame(root)
titleLabel = ttk.Label(mainFrame)
secondaryLabel = ttk.Label(mainFrame)
quitButton = ttk.Button(mainFrame)
createButton = ttk.Button(mainFrame)
listButton = ttk.Button(mainFrame)
deleteButton = ttk.Button(mainFrame)
editButton = ttk.Button(mainFrame)
firstNameEntry = ttk.Entry(mainFrame)
lastNameEntry = ttk.Entry(mainFrame)

mainFrame.grid()
titleLabel.grid()
secondaryLabel.grid()
quitButton.grid()
createButton.grid()
listButton.grid()
deleteButton.grid()
editButton.grid()
firstNameEntry.grid()
lastNameEntry.grid()

firstNameEntry.grid_remove()
lastNameEntry.grid_remove()

def fileAccess(mode, row):
    pass

def createItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber
    secondaryLabel.configure(text = "Item Rental | Logging a Rented Item")
    createButton.grid_remove()
    listButton.grid_remove()
    deleteButton.grid_remove()
    editButton.grid_remove()

    firstNameEntry.grid()
    lastNameEntry.grid()

def listItems():
    global firstRow
    

def deleteItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber
    

def editItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber
    

def quitProgram():
    if mb.askyesno(title = "Julie's Party Hire Store", message = "Are you sure you want to quit?") == True:
        root.destroy()

def main():
    global firstRow

    titleLabel.configure(text = "Julie's Hire Database")
    secondaryLabel.configure(text = "Commands to run")
    quitButton.configure(text = "Quit", command = quitProgram)
    createButton.configure(text = "Log a rented item", command = createItem)
    listButton.configure(text = "Show all currently rented items", command = listItems)
    deleteButton.configure(text = "Log a returned item", command = deleteItem)
    editButton.configure(text = "Edit a rented item log", command = editItem)
    
    if os.path.exists("AS91897ROW.txt") == False:
        rowFile = open("AS91897ROW.txt","a")
        rowFile.write("1")
        rowFile.close()
    if os.path.exists("AS91897DATA.txt") == False:
        dataFile = open("AS91897DATA.txt","a")
        dataFile.write("FIRST NAME,LAST NAME,HIRED ITEM,NUM HIRES,RECEIPT\n")
        dataFile.close()
    
    while True:
        rowFile = open("AS91897ROW.txt","r")
        firstRow = rowFile.readline().split()
        rowFile.close()
        
        root.update_idletasks()
        root.update()

if __name__ == "__main__":
    main()
