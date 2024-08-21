from tkinter import *
from tkinter import Tk as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import font
from functools import partial
import os
import re

root = tk()
style = ttk.Style()

# HELVETICA - MICROSOFT SANS SERIF - SEGOE UI

fontFamily = "Helvetica"

titleFont = font.Font(family = fontFamily, name = "titleFont", size = 20, weight = "bold")
headerFont = font.Font(family = fontFamily, name = "headerFont", size = 15, weight = "bold")
mainFont = font.Font(family = fontFamily, name = "mainFont", size = 10)
italFont = font.Font(family = fontFamily, name = "italFont", size = 9, slant = "italic")

print(font.font_families())

style.configure("Title.TLabel", font = titleFont, padding = 5)
style.configure("Header.TLabel", font = headerFont, padding = 2.5)
style.configure("Main.TLabel", font = mainFont, padding = 2.5)
style.configure("Main.TButton", font = mainFont, padding = 5, width = 30, height = 2.5)
style.configure("Sub.TButton", font = italFont, padding = 0, width = 2.25, height = 0.75)

root.title("Julie's Party Hire Store")
mainFrame = ttk.Frame(root, padding = 7.5, width = 150, height = 150)
secondaryFrame = ttk.Frame(mainFrame, padding = 5)
titleLabel = ttk.Label(mainFrame, style = "Title.TLabel")
secondaryLabel = ttk.Label(secondaryFrame, style = "Header.TLabel")
quitButton = ttk.Button(root, style = "Sub.TButton")
createButton = ttk.Button(secondaryFrame, style = "Main.TButton")
listButton = ttk.Button(secondaryFrame, style = "Main.TButton")
deleteButton = ttk.Button(secondaryFrame, style = "Main.TButton")
editButton = ttk.Button(secondaryFrame, style = "Main.TButton")
firstNameEntry = ttk.Entry(secondaryFrame)
lastNameEntry = ttk.Entry(secondaryFrame)
rentedItemEntry = ttk.Combobox(secondaryFrame)
numberItemsEntry = ttk.Spinbox(secondaryFrame, from_ = 1, to = 1000, increment = 1)
receiptEntry = ttk.Entry(secondaryFrame)
firstNameLabel = ttk.Label(secondaryFrame)
lastNameLabel = ttk.Label(secondaryFrame)
rentedItemLabel = ttk.Label(secondaryFrame)
numberItemsLabel = ttk.Label(secondaryFrame)
receiptLabel = ttk.Label(secondaryFrame)
actionButton = ttk.Button(mainFrame)

mainFrame.grid(row = 0, column = 0, sticky = "news")
secondaryFrame.grid(row = 2, columnspan = 2, sticky = "news")
titleLabel.grid(row = 0, column = 0, columnspan = 2)
secondaryLabel.grid(row = 0, columnspan = 2)
quitButton.grid(row = 0, column = 0, sticky = "ne")
createButton.grid(row = 1, column = 0)
listButton.grid(row = 1, column = 1)
deleteButton.grid(row = 2, column = 0)
editButton.grid(row = 2, column = 1)


root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
mainFrame.columnconfigure(0, weight = 1)
mainFrame.columnconfigure(1, weight = 1)
mainFrame.rowconfigure(0, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
mainFrame.rowconfigure(2, weight = 1)
secondaryFrame.columnconfigure(0, weight = 1, pad = 10)
secondaryFrame.columnconfigure(1, weight = 1, pad = 10)
secondaryFrame.rowconfigure(0, weight = 1, pad = 5)
secondaryFrame.rowconfigure(1, weight = 1, pad = 5)
secondaryFrame.rowconfigure(2, weight = 1, pad = 5)

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
                receiptNumber = int(row) * len(firstName) * len(lastName) * len(rentedItem) * numberItems * ord(firstName[0]) * ord(lastName[0])
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
            confirm = mb.askyesnocancel(title = "Julie's Party Hire Store", message = "Are you sure you want to continue?", detail = "Press No to go back, and Cancel to return to main menu.")
            if confirm == False:
                return
            elif confirm == True:
                firstName = str(firstName.get()).title().replace(" ","").replace(",","")
                lastName = str(lastName.get()).title().replace(" ","").replace(",","")
                rentedItem = str(rentedItem.get()).title().replace(",","")
                numberItems = int(numberItems.get())
                print(firstName)
                print(lastName)
                print(firstName[0])
                print(lastName[0])
                receiptNumber = int(row) * len(firstName) * len(lastName) * len(rentedItem) * numberItems * ord(firstName[0]) * ord(lastName[0])
                print(f"New Receipt: {receiptNumber}")
                mb.showinfo(title = "Julie's Party Hire Store", message = str("Your edit has been recorded. Receipt: " + str(receiptNumber)))
            
                dataString = ""
                dataFile = open("AS91897DATA.txt","r")
                dataArray = dataFile.read()
                dataArray = re.split(', |\n', dataArray)
                dataArray[int(row)] = firstName + "," + lastName + "," + rentedItem + "," + str(numberItems) + "," + str(receiptNumber)
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
            actionButton.grid_remove()
            secondaryLabel.configure(text = "Commands to run")
            createButton.grid()
            listButton.grid()
            deleteButton.grid()
            editButton.grid()
            return

def checkNum(val):
    return re.match(r"^[0-9]*$", val) is not None
checkNumWrapper = (root.register(checkNum), "%P")

def checkStr(val):
    return re.match(r"^([A-z]|\s)*$", val) is not None
checkStrWrapper = (root.register(checkStr), "%P")

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
    firstNameEntry.configure(textvariable = firstName, validate = "key", validatecommand = checkStrWrapper)
    lastNameEntry.configure(textvariable = lastName, validate = "key", validatecommand = checkStrWrapper)
    rentedItemEntry.configure(values = itemsList, validate = "key", textvariable = rentedItem, validatecommand = checkStrWrapper)
    numberItemsEntry.configure(textvariable = numberItems, validate = "key", validatecommand = checkNumWrapper)
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
    firstNameEntry.configure(textvariable = firstName, validate = "key", validatecommand = checkStrWrapper)
    lastNameEntry.configure(textvariable = lastName, validate = "key", validatecommand = checkStrWrapper)
    rentedItemEntry.configure(values = itemsList, textvariable = rentedItem, validate = "key", validatecommand = checkStrWrapper)
    numberItemsEntry.configure(textvariable = numberItems, validate = "key", validatecommand = checkNumWrapper)
    receiptEntry.configure(textvariable = receiptNumber, validate = "key", validatecommand = checkNumWrapper)
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
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber

    firstName = str(firstName.get()).title().replace(" ","").replace(",","")
    lastName = str(lastName.get()).title().replace(" ","").replace(",","")
    rentedItem = str(rentedItem.get()).title().replace(",","")
    numberItems = int(numberItems.get())
    receiptNumber = int(receiptNumber.get())
    if len(firstName) != 0 and len(lastName) != 0 and len(rentedItem) != 0 and numberItems != 0:
        rowNum = float(receiptNumber / len(firstName) / len(lastName) / len(rentedItem) / numberItems / ord(firstName[0]) / ord(lastName[0]))
    else:
        rowNum = 0.5
    
    if str(int(rowNum)) in firstRow and rowNum.is_integer():
        editFunc = partial(fileAccess, "w", rowNum)
        
        firstName = StringVar()
        lastName = StringVar()
        rentedItem = StringVar()
        numberItems = IntVar()

        firstNameEntry.configure(textvariable = firstName, validate = "key", validatecommand = checkStrWrapper)
        lastNameEntry.configure(textvariable = lastName, validate = "key", validatecommand = checkStrWrapper)
        rentedItemEntry.configure(values = itemsList, textvariable = rentedItem, validate = "key", validatecommand = checkStrWrapper)
        numberItemsEntry.configure(textvariable = numberItems, validate = "key", validatecommand = checkNumWrapper)
        firstNameLabel.configure(text = "Customer's new First name:")
        lastNameLabel.configure(text = "Customer's new Last name:")
        rentedItemLabel.configure(text = "The new item that was hired:")
        numberItemsLabel.configure(text = "The new amount of items hired:")
        actionButton.configure(text = "Confrm Changes", command = editFunc)
        receiptLabel.grid_remove()
        receiptEntry.grid_remove()
    else:
        mb.showerror(title = "Julie's Party Hire Store", message = "The data you entered is incorrect. Please double check all your information is accurate.")
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

def editItem():
    global firstRow, firstName, lastName, rentedItem, numberItems, receiptNumber
    firstName = StringVar()
    lastName = StringVar()
    rentedItem = StringVar()
    numberItems = IntVar()
    receiptNumber = IntVar()
    
    secondaryLabel.configure(text = "Item Rental | Editing a hired Item")
    createButton.grid_remove()
    listButton.grid_remove()
    deleteButton.grid_remove()
    editButton.grid_remove()
    firstNameEntry.configure(textvariable = firstName, validate = "key", validatecommand = checkStrWrapper)
    lastNameEntry.configure(textvariable = lastName, validate = "key", validatecommand = checkStrWrapper)
    rentedItemEntry.configure(values = itemsList, textvariable = rentedItem, validate = "key", validatecommand = checkStrWrapper)
    numberItemsEntry.configure(textvariable = numberItems, validate = "key", validatecommand = checkNumWrapper)
    receiptEntry.configure(textvariable = receiptNumber, validate = "key", validatecommand = checkNumWrapper)
    firstNameLabel.configure(text = "Customer's First name:")
    lastNameLabel.configure(text = "Customer's Last name:")
    rentedItemLabel.configure(text = "Item that was hired:")
    numberItemsLabel.configure(text = "The amount of items hired:")
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
        os._exit(os.EX_OK)
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
        itemsList = list(dict.fromkeys(itemsList))
        
        dataFile.close()
        
        root.update_idletasks()
        root.update()

if __name__ == "__main__":
    main()
