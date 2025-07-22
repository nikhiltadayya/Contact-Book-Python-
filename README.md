# 📒 Contact Book Management System

This is a simple **Contact Book project using MySQL** to store, add, display, search, and delete contacts.

## 💻 **Features**

1. **Add Contact** – Save a new contact with name, phone, and email.
2. **Display Contacts** – View all saved contacts.
3. **Search Contact** – Find a contact by name or phone.
4. **Delete Contact** – Remove a contact from the database.
5. **Exit** – Exit the application.

## 🗃️ **Database Structure**

**Database Name:** `contact_book`

**Table:** `contacts`

| Column | Type                              | Description          |
| ------ | --------------------------------- | -------------------- |
| id     | INT (Auto Increment, Primary Key) | Contact ID           |
| name   | VARCHAR(100)                      | Contact Name         |
| phone  | VARCHAR(20)                       | Contact Phone Number |
| email  | VARCHAR(100)                      | Contact Email        |

### 📂 **Sample SQL Code**

```sql
CREATE DATABASE contact_book;
USE contact_book;

CREATE TABLE contacts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

SELECT * FROM contacts;
```

## 🖥️ **Sample Output**

```
1. Add Contact
2. Display Contacts
3. Search contact
4. Delete Contact
5. Exit
Enter choice: 1
Enter name: nikhil
Enter phone numbers: 7887386542
Enter email: nikhiltadayya@2003
Contact added successfully!
```

## 🚀 **Usage**

* Execute the SQL script to create the database and table.
* Run your program (C/Python/Java – depending on your implementation) to interact with MySQL for adding and managing contacts.

---

Let me know if you want **badges, GitHub topics, or project setup instructions** for this repository before uploading today.
