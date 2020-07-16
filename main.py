import os
import sqlite3
import new_password
import search_all
import delete

ADMIN_PASSWORD = 'admin'

connect = input('Enter your password: \n')

while connect != ADMIN_PASSWORD:
    connect = input("Enter your Password: \n")
    if connect =='q':break
    os.system('clear')
    
conn = sqlite3.connect('database.db')
c= conn.cursor()
print()

while True:
    os.system('clear')
    print("\nWelcome to the Password Vault\n")
    print("\nCommands: ")
    print("s= see all Password")
    print("n= New Password")
    print("d= Delete Password")
    print("q= Quit")
    
    userInput= input("Enter Command: ")
    if userInput == 's':
        search_all.search()
    elif userInput == 'n':
        new_password.new()
    elif userInput == 'd':
        delete.delete_pass()
    elif userInput == 'q':
        break