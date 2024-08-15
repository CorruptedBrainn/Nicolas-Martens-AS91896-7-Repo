from tkinter import *
from tkinter import Tk as tk
from tkinter import ttk
from tkinter import messagebox as mb
from functools import partial
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
rentedItemEntry = ttk.Combobox(mainFrame)
numberItemsEntry = ttk.Spinbox(mainFrame, from_ = 1, to = 1000, increment = 1)
receiptEntry = ttk.Entry(mainFrame)
firstNameLabel = ttk.Label(mainFrame)
lastNameLabel = ttk.Label(mainFrame)
rentedItemLabel = ttk.Label(mainFrame)
numberItemsLabel = ttk.Label(mainFrame)
receiptLabel = ttk.Label(mainFrame)
actionButton = ttk.Button(mainFrame)

mainFrame.grid()
titleLabel.grid()
secondaryLabel.grid()
quitButton.grid()
createButton.grid()
listButton.grid()
deleteButton.grid()
editButton.grid()

def fileAccess(mode, row):
    global firstName, lastName, rentedItem, numberItems, receiptNumber
    match mode:
        case "d":
            confirm = mb.askyesnocancel(title = "Julie's Party Hire Store", message = "Are you sure you want to continue?", detail = "Press No to go back, and Cancel to return to main menu.")
            if confirm == False:
                return
            elif confirm == True:
                firstName = str(firstName.get()).title().replace(" ","").replace(",","")
                lastName = str(lastName.get()).title().replace(" ","").replace(",","")
                rentedItem = str(rentedItem.get()).title().replace(",","")
                numberItems = int(numberItems.get())
                receiptNumber = int(receiptNumber.get())
                rowNum = float(receiptNumber / len(firstName) / len(lastName) / len(rentedItem) / numberItems / ord(firstName[0]) / ord(lastName[0]))
                if str(int(rowNum)) in firstRow and rowNum.is_integer():
                    rowNum = str(int(rowNum))
                    rowFile = open("AS91897ROW.txt","w")
                    firstRow.remove(rowNum)
                    rowNum = ""
                    for i in firstRow:
                        rowNum = rowNum + " " + str(i)
                    rowFile.write(rowNum.strip())
                    rowFile.close()
                else:
                    mb.showerror(title = "Julie's Party Hire Store", message = "The data you entered is incorrect. Please double check all your information is accurate.")
                    return
                mb.showinfo(title = "Julie's Party Hire Store", message = "Your delete has been recorded.")
                
            firstNameLabel.grid_remove()
            firstNameEntry.grid_remove()
            lastNameLabel.grid_remove()
            lastNameEntry.grid_remove()
            rentedItemLabel.grid_remove()
            rentedItemEntry.grid_remove()
            numberItemsLabel.grid_remove()
            numberItemsEntry.grid_remove()
            receiptLabel.grid_remove()
            receiptEntry.grid_remove()
            actionButton.grid_remove()
            secondaryLabel.configure(text = "Commands to run")
            createButton.grid()
            listButton.grid()
            deleteButton.grid()
            editButton.grid()
            return
        case "a":
            confirm = mb.askyesnocancel(title = "Julie's Party Hire Store", message = "Are you sure you want to continue?", detail = "Press No to go back, and Cancel to return to main menu.")
            if confirm == False:
                return
            elif confirm == True:
                firstName = str(firstName.get()).title().replace(" ","").replace(",","")
                lastName = str(lastName.get()).title().replace(" ","").replace(",","")
                rentedItem = str(rentedItem.get()).title().replace(",","")
                numberItems = int(numberItems.get())
                receiptNumber = int(firstRow[-1]) * len(firstName) * len(lastName) * len(rentedItem) * numberItems * ord(firstName[0]) * ord(lastName[0])
                print(f"Receipt: {receiptNumber}")
                mb.showinfo(title = "Julie's Party Hire Store", message = str("Your entry has been recorded. Receipt: " + str(receiptNumber)))
            
                dataFile = open("AS91897DATA.txt",mode)
                localVar = firstName + "," + lastName + "," + rentedItem + "," + str(numberItems) + "," + str(receiptNumber) + "\n"
                dataFile.write(localVar)
                dataFile.close()
            
                rowFile = open("AS91897ROW.txt",mode)
                row = " "+str(int(row) + 1)
                rowFile.write(str(row))
                rowFile.close()
                
            firstNameLabel.grid_remove()
            firstNameEntry.grid_remove()
            lastNameLabel.grid_remove()
            lastNameEntry.grid_remove()
            rentedItemLabel.grid_remove()
            rentedItemEntry.grid_remove()
            numberItemsLabel.grid_remove()
            numberItemsEntry.grid_remove()
            actionButton.grid_remove()
            secondaryLabel.configure(text = "Commands to run")
            createButton.grid()
            listButton.grid()
            deleteButton.grid()
            editButton.grid()
            return
        case "r":
            message = "List of Hired Items:\n\n"
            print("Hired Items:\n")
            dataFile = open("AS91897DATA.txt",mode)
            i = 0
            for x in range(int(row[-1])):
                dataPrint = dataFile.readline().split(",")
                if str(x) not in row:
                    continue
                i += 1
                print(f"Hire {i}\t|\tFull Name: {dataPrint[0]} {dataPrint[1]}")
                message = message + "Hire " + str(i) + "\t|\tFull Name: " + dataPrint[0] + " " + dataPrint[1] + "\n"
                print(f"\t|\tItems Rented: {dataPrint[3]} {dataPrint[2]}")
                message = message + "\t|\tItems Rented: " + dataPrint[3] + " " + dataPrint[2] + "\n"
                print(f"\t|\tReceipt: {dataPrint[4]}")
                message = message + "\t|\tReceipt: " + dataPrint[4] + "\n"
            mb.showinfo(title = "Julie's Party Store", message = message)
            dataFile.close()
            return
        case "w":
            dataString = ""
            dataFile = open("AS91897DATA.txt","r")
            dataArray = dataFile.read()
            dataArray = re.split(', |\n', dataArray)
            dataArray[int(rowNum)] = firstName + "," + lastName + "," + rentedItem + "," + str(numberItems) + "," + str(receiptNumber)
            dataFile.close()
            for x in dataArray:
                dataString = dataString + x + "\n"
            dataFile = open("AS91897DATA.txt",mode)
            dataFile.write(dataString)
            dataFile.close()
            
            firstNameLabel.grid_remove()
            firstNameEntry.grid_remove()
            lastNameLabel.grid_remove()
            lastNameEntry.grid_remove()
            rentedItemLabel.grid_remove()
            rentedItemEntry.grid_remove()
            numberItemsLabel.grid_remove()
            numberItemsEntry.grid_remove()
            receiptLabel.grid_remove()
            receiptEntry.grid_remove()
            actionButton.grid_remove()
            secondaryLabel.configure(text = "Commands to run")
            createButton.grid()
            listButton.grid()
            deleteButton.grid()
            editButton.grid()
            return

def createItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber, itemsList
    firstName = StringVar()
    lastName = StringVar()
    rentedItem = StringVar()
    numberItems = IntVar()

    createFunc = partial(fileAccess, "a", firstRow[-1])
    
    secondaryLabel.configure(text = "Item Rental | Logging a Hired Item")
    createButton.grid_remove()
    listButton.grid_remove()
    deleteButton.grid_remove()
    editButton.grid_remove()
    firstNameEntry.configure(textvariable = firstName)
    lastNameEntry.configure(textvariable = lastName)
    rentedItemEntry.configure(values = itemsList, textvariable = rentedItem)
    numberItemsEntry.configure(textvariable = numberItems)
    firstNameLabel.configure(text = "Customer's First name:")
    lastNameLabel.configure(text = "Customer's Last name:")
    rentedItemLabel.configure(text = "Item that has been hired:")
    numberItemsLabel.configure(text = "How many items have been hired:")
    actionButton.configure(text = "Confirm Changes", command = createFunc)

    firstNameLabel.grid()
    firstNameEntry.grid()
    lastNameLabel.grid()
    lastNameEntry.grid()
    rentedItemLabel.grid()
    rentedItemEntry.grid()
    numberItemsLabel.grid()
    numberItemsEntry.grid()
    actionButton.grid()
    return

def listItems():
    global firstRow
    fileAccess("r",firstRow)
    return

def deleteItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber
    firstName = StringVar()
    lastName = StringVar()
    rentedItem = StringVar()
    numberItems = IntVar()
    receiptNumber = IntVar()

    delFunc = partial(fileAccess, "d", "0")
    
    secondaryLabel.configure(text = "Item Rental | Logging a Returned Item")
    createButton.grid_remove()
    listButton.grid_remove()
    deleteButton.grid_remove()
    editButton.grid_remove()
    firstNameEntry.configure(textvariable = firstName)
    lastNameEntry.configure(textvariable = lastName)
    rentedItemEntry.configure(values = itemsList, textvariable = rentedItem)
    numberItemsEntry.configure(textvariable = numberItems)
    receiptEntry.configure(textvariable = receiptNumber)
    firstNameLabel.configure(text = "Customer's First name:")
    lastNameLabel.configure(text = "Customer's Last name:")
    rentedItemLabel.configure(text = "Item that has been returned:")
    numberItemsLabel.configure(text = "How many items have been returned:")
    receiptLabel.configure(text = "The receipt number of the transaction:")
    actionButton.configure(text = "Confirm Changes", command = delFunc)

    firstNameLabel.grid()
    firstNameEntry.grid()
    lastNameLabel.grid()
    lastNameEntry.grid()
    rentedItemLabel.grid()
    rentedItemEntry.grid()
    numberItemsLabel.grid()
    numberItemsEntry.grid()
    receiptLabel.grid()
    receiptEntry.grid()
    actionButton.grid()
    return

def editItemCont():
    

def editItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber
    firstName = StringVar()
    lastName = StringVar()
    rentedItem = StringVar()
    numberItems = IntVar()
    receiptNumber = IntVar()

    editFunc = partial(fileAccess, "w", "0")
    
    secondaryLabel.configure(text = "Item Rental | Logging a Returned Item")
    createButton.grid_remove()
    listButton.grid_remove()
    deleteButton.grid_remove()
    editButton.grid_remove()
    firstNameEntry.configure(textvariable = firstName)
    lastNameEntry.configure(textvariable = lastName)
    rentedItemEntry.configure(values = itemsList, textvariable = rentedItem)
    numberItemsEntry.configure(textvariable = numberItems)
    receiptEntry.configure(textvariable = receiptNumber)
    firstNameLabel.configure(text = "Customer's First name:")
    lastNameLabel.configure(text = "Customer's Last name:")
    rentedItemLabel.configure(text = "Item that was hired:")
    numberItemsLabel.configure(text = "The amountof items hired:")
    receiptLabel.configure(text = "The receipt number of the transaction:")
    actionButton.configure(text = "Continue", command = editItemCont)

    firstNameLabel.grid()
    firstNameEntry.grid()
    lastNameLabel.grid()
    lastNameEntry.grid()
    rentedItemLabel.grid()
    rentedItemEntry.grid()
    numberItemsLabel.grid()
    numberItemsEntry.grid()
    receiptLabel.grid()
    receiptEntry.grid()
    actionButton.grid()
    return

def quitProgram():
    if mb.askyesno(title = "Julie's Party Hire Store", message = "Are you sure you want to quit?") == True:
        root.destroy()
    return

def main():
    global firstRow, itemsList

    titleLabel.configure(text = "Julie's Hire Database")
    secondaryLabel.configure(text = "Commands to run")
    quitButton.configure(text = "Quit", command = quitProgram)
    createButton.configure(text = "Log a rented item", command = createItem)
    listButton.configure(text = "Show all currently rented items", command = listItems)
    deleteButton.configure(text = "Log a returned item", command = deleteItem)
    editButton.configure(text = "Edit a rented item log", command = editItem)
    
    if os.path.exists("AS91897ROW.txt") == False:
        rowFile = open("AS91897ROW.txt", "a")
        rowFile.write("1")
        rowFile.close()
    if os.path.exists("AS91897DATA.txt") == False:
        dataFile = open("AS91897DATA.txt", "a")
        dataFile.write("FIRST NAME,LAST NAME,HIRED ITEM,NUM HIRES,RECEIPT\n")
        dataFile.close()
    
    while True:
        rowFile = open("AS91897ROW.txt","r")
        firstRow = rowFile.readline().split()
        rowFile.close()

        dataFile = open("AS91897DATA.txt", "r")
        tempArray = dataFile.read().replace("\n",",").strip(",").split(",")
        
        itemsList = ["placeholder"]
        itemsList.clear()
        
        for i in range(len(tempArray)):
            if i % 5 == 2 and i > 5:
                itemsList.append(tempArray[i])
        dataFile.close()
        
        root.update_idletasks()
        root.update()

if __name__ == "__main__":
    main()
