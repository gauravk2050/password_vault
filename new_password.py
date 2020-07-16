import sqlite3


conn=sqlite3.connect('database.db')
c= conn.cursor()

def new():
    conn= sqlite3.connect('database.db')
    c= conn.cursor()
    website = input('Enter Website: ')
    username = input("Username: ")
    password = input('Password: ')
    
    c.execute("""INSERT INTO passwords
    (website, username, password) VALUES
    (?, ?, ?)
    """,(website,username,password))
    conn.commit()
    c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    for row in result:
        print(row)
    conn.close()
    print("Press Enter to Exit")
    return