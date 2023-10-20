# contact-book-project

## Build a Contact Book With Python, PyQt, and SQLite

- ![Perisan Document ( مستند فارسی )](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Docs/README-PERSIAN.md)
 
### Project Overview

- To build our contact book application, we need to organize the code into modules and packages and give our project a coherent structure. In this project, we’ll use the following directories and files structure:
  
    ```
    contact_book_project/
    │
    ├── contacts_book/
    │   ├── __init__.py
    │   ├── views.py
    │   ├── database.py
    │   ├── main.py
    │   └── model.py
    │
    ├── requirements.txt
    ├── README.md
    └── contact_book.py
    ```

***

### Step 1: Creating the Contact Book’s Skeleton App With PyQt

- Structuring the Contact Book Project
- Creating the Application’s Main Window
- Coding and Running the Application

In this first step, we’ll create a minimal but functional PyQt GUI application to provide the foundation on which we’ll start building the contact book. We’ll also create the minimal required project structure, including the project’s main package and an entry-point script to run the application.

![Contact Book Step 1](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%201.png)

***

### Step 2: Building the Contact Book’s GUI With Python

Now that you’ve built the skeleton of your contact book application, you can start coding the main window’s GUI. At the end of this section, you’ll have completed the required steps to create the GUI of your contact book using Python and PyQt.

![Contact Book Step 2](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%202.png)

***

### Step 3: Setting Up the Contact Book’s Database

- Connecting to the Database With PyQt and SQLite
- Creating the contacts Table
- Testing the Contact Book’s Database

At this point, we’ve created a PyQt application and its main window’s GUI to build our contact book project. In this section, we’ll write code to define how the application connects to the contact database. To complete this step, we’ll use SQLite to handle the database and PyQt’s SQL support to connect the application to the database and to work with our contact data.

| Column  | Content |
| ------------- | ------------- |
| id  | An integer with the table’s primary key  |
| name  | A string with the name of a contact  |
| job  | A string with the job title of a contact  |
| email  | A string with the email of a contact  |

***

### Step 4: Displaying and Updating Existing Contacts

- Creating a Model to Handle the Contact Data
- Connecting the Model to the View
- Displaying and Updating Contacts

To display our contact data in the application’s main window, we can use QTableView. This class is part of PyQt’s Model-View architecture and provides a robust and efficient way of displaying items from a PyQt model object.

![Contact Book Step 4](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%204.png)

***

### Step 5: Creating New Contacts

- Creating the Add Contact Dialog
- Launching the Add Contact Dialog
- Processing the Add Dialog’s Data in the Model

At this step, our contact book application provides functionality to load, display, and update the information about our contacts. Even though we’re able to modify and update the contact information, we can neither add nor remove contacts from the list. In this section, we’ll provide the required functionality to add new contacts to the database, using a pop-up dialog to enter the new information.

![Contact Book Step 5-1](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%205-1.png)

We define a conditional statement that checks if the user has provided data for each field in the dialog. If not, then the dialog shows an error message that warns the user about the missing data.

![Contact Book Step 5-3](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%205-3.png)

And if the user has provided data for each field in the dialog, then it adds the contact to the database by clicking OK.

![Contact Book Step 5-2](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%205-2.png)

***

### Step 6: Deleting Existing Contacts

- Deleting Selected Contacts
- Clearing the Contact Database

The final feature we’ll add to the contact book application is the ability to remove contacts from the database using the GUI. In this section, we’ll first add the capability to delete a single contact at a time. Then we’ll add code to remove all the contacts from the database.

Now when we select a contact from the table view and click Delete, we’re presented with a warning message.

![Contact Book Step 6-1](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%206-1.png)

If we click the message dialog’s OK button, then the application removes the selected contact from the database, updating the table view accordingly. (Removed Sahar from Database)

![Contact Book Step 6-2](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%206-2.png)

And to clear all the contacts at the same time, we first create a message dialog to ask the user to confirm the removing operation.

![Contact Book Step 6-3](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%206-3.png)

If the user confirms the operation by clicking OK, then it removes all the contacts from the database.

![Contact Book Step 6-4](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Assets/Contact%20Book%20Step%206-4.png)
