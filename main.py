import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        database="contact_book",
        user="root",
        auth_plugin='mysql_native_password',
        password="Nikhil")

#
def add_contact():
    name=input("Enter name:")
    phone=input("Enter phone numbers:")
    email=input("Enter email:")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO contacts (name,phone,email) VALUES(%s,%s,%s)",(name,phone,email))
    conn.commit()
    print("Contact added successfully!")
    conn.close()


#
def display_contact():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT name,phone,email FROM contacts")
    for row in cursor.fetchall():
        print(f"Name:{row[0]}, Phone:{row},Email:{row[2]}")
    conn.close()

#
def search_contact():
    name=input("Enter name to search:")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = %s",(name,))
    contact=cursor.fetchone()
    if contact:
        print(f"Name:{contact[0]},Phone:{contact[1]},Email:{contact[2]}")
    else:
        print("Contact not found")  
    conn.close()  

# delete contact
def delete_contact():
    name=input("Enter name to delete:")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE name = %s",(name,))
    conn.commit()
    print("Contact deleted successfully!")
    conn.close()

#
def main():
    while True:
        print("\n1.Add Contact\n2.Display Contacts\n3. Search contact\n4. Delete Contact\n5.Exit")
        choice=input("Enter choice:")
        if choice =="1":
            add_contact()
        elif choice=="2":
            display_contact() 
        elif choice=="3":
            search_contact()
        elif choice=="4":
            delete_contact()
        elif choice=="5":
            print("Goodbye!")   
        else:
            print("Invaild choice , try again.")   
main()             

