import os
import re

def fileAccess(mode, row):
    match mode:
        case "a":
            dataFile = open("AS91897DATA.txt",mode)
            localVar = firstName + "," + lastName + "," + rentedItem + "," + str(numberItems) + "," + str(receiptNumber) + "\n"
            dataFile.write(localVar)
            dataFile.close()
            rowFile = open("AS91897ROW.txt",mode)
            row = " "+str(int(row) + 1)
            rowFile.write(str(row))
            rowFile.close()
        case "r":
            dataFile = open("AS91897DATA.txt",mode)
            i = 0
            for x in range(int(row[-1])):
                dataPrint = dataFile.readline().split(",")
                if str(x) not in row:
                    continue
                i += 1
                print(f"Hire {i}\t|\tFull Name: {dataPrint[0]} {dataPrint[1]}")
                print(f"\t|\tItems Rented: {dataPrint[3]} {dataPrint[2]}")
                print(f"\t|\tReceipt: {dataPrint[4]}")
            dataFile.close()
        case "w":
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
            
def createItem(firstRow):
    global firstName, lastName, rentedItem, numberItems, receiptNumber
    print("You've chosen to log a rented item. Please enter the below details.")
    firstName = str(input("Customer's First Name: "))
    lastName = str(input("Customer's Surname: "))
    rentedItem = str(input("Item that has been rented: "))
    numberItems = int(input("How many items have been hired: "))
    firstName = firstName.title().replace(" ","").replace(",","")
    lastName = lastName.title().replace(" ","").replace(",","")
    rentedItem = rentedItem.title().replace(",","")
    receiptNumber = int(firstRow[-1]) * len(firstName) * len(lastName) * len(rentedItem) * numberItems * ord(firstName[0]) * ord(lastName[0])
    print(f"Receipt Number: {receiptNumber}")
    fileAccess("a",firstRow[-1])
    return

def listItems(firstRow):
    print("You've chosen to print all currently rented items. Below are all the hires.")
    fileAccess("r",firstRow)
    return

def deleteItem(firstRow):
    global firstName, lastName, rentedItem, numberItems, receiptNumber
    print("You've chosen to log a returned item. Please confirm the details below.")
    firstName = str(input("Customer's First Name: "))
    lastName = str(input("Customer's Surname: "))
    rentedItem = str(input("Item that has been returned: "))
    numberItems = int(input("The amount of items that were hired: "))
    receiptNumber = int(input("The receipt number of the interaction: "))
    firstName = firstName.title().replace(" ","").replace(",","")
    lastName = lastName.title().replace(" ","").replace(",","")
    rentedItem = rentedItem.title().replace(",","")
    rowNum = receiptNumber / len(firstName) / len(lastName) / len(rentedItem) / numberItems / ord(firstName[0]) / ord(lastName[0])
    rowNum = str(int(rowNum))
    if rowNum in firstRow:
        rowFile = open("AS91897ROW.txt","w")
        firstRow.remove(rowNum)
        rowNum = ""
        for i in firstRow:
            rowNum = rowNum + " " + str(i)
        rowFile.write(rowNum.strip())
        rowFile.close()
    else:
        print("There was an incorrect detail. The data you entered does not exist.")
    return

def editItem(firstRow):
    global firstName, lastName, rentedItem, numberItems, receiptNumber
    print("You've chosen to edit a rented item. Please confirm the details below.")
    firstName = str(input("Customer's First Name: "))
    lastName = str(input("Customer's Surname: "))
    rentedItem = str(input("Item that was hired: "))
    numberItems = int(input("The amount of items that were hired: "))
    receiptNumber = int(input("The receipt number of the interaction: "))
    firstName = firstName.title().replace(" ","").replace(",","")
    lastName = lastName.title().replace(" ","").replace(",","")
    rentedItem = rentedItem.title().replace(",","")
    rowNum = receiptNumber / len(firstName) / len(lastName) / len(rentedItem) / numberItems / ord(firstName[0]) / ord(lastName[0])
    rowNum = str(int(rowNum))
    if rowNum in firstRow:
        print("Now enter the new details of the hire.")
        firstName = str(input("Customer's First Name: "))
        lastName = str(input("Customer's Surname: "))
        rentedItem = str(input("Item that was hired: "))
        numberItems = int(input("The amount of items that were hired: "))
        receiptNumber = int(rowNum) * len(firstName) * len(lastName) * len(rentedItem) * numberItems * ord(firstName[0]) * ord(lastName[0])
        print(f"New Receipt Number: {receiptNumber}")
        fileAccess("w",rowNum)
    else:
        print("There was an incorrect detail. The data you entered does not exist.")
    return

def quitProgram():
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
