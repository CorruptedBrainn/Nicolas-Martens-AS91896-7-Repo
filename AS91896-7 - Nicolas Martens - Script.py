from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

def create():
    print("Create")
    return

def list():
    print("List")
    return

def delete():
    print("Delete")
    return

def edit():
    print("Edit")
    return

def quit():
    print("Quit")
    return

def main():
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
        action = input("\nEnter Command: ")
        action = action.lower().replace(" ","")
        match action:
            case action if action in [commands[0], commands[1]]:
                create()
            case action if action in [commands[2], commands[3]]:
                list()
            case action if action in [commands[4], commands[5]]:
                delete()
            case action if action in [commands[6], commands[7]]:
                edit()
            case action if action in [commands[8], commands[9]]:
                quit()
            case _:
                print("\nError, Command Entered is Invalid")
                continue

if __name__ == "__main__":
    main()
