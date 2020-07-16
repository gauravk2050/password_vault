'''
This python file is used to delete the password form the database
'''

import os
import sqlite3

def delete_pass():
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    print(conn)
    print("\nYou are deletinf your password by website name")
    user_input = input("Enter website: ")

    c.execute("""DELETE FROM passwords
         WHERE website = ?
         """,(user_input,))
    conn.commit()
    conn.close()
    print("Your password has been deleted")
    input('PRess Enter to Exit')
    os.system("clear")
    return
