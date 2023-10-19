# contact-book-project

Build a Contact Book With Python, PyQt, and SQLite

Step 1: Creating the Contact Book’s Skeleton App With PyQt

- * Structuring the Contact Book Project
- * Creating the Application’s Main Window
- * Coding and Running the Application

- In this first step, we’ll create a minimal but functional PyQt GUI application to provide the foundation on which we’ll start building the contact book.
We’ll also create the minimal required project structure, including the project’s main package and an entry-point script to run the application.

![Contact Book Step 1](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Files/Contact%20Book%20Step%201.png)


Step 2: Building the Contact Book’s GUI With Python

- Now that you’ve built the skeleton of your contact book application, you can start coding the main window’s GUI.
At the end of this section, you’ll have completed the required steps to create the GUI of your contact book using Python and PyQt.

![Contact Book Step 1](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Files/Contact%20Book%20Step%202.png)


Step 3: Setting Up the Contact Book’s Database

- * Connecting to the Database With PyQt and SQLite
- * Creating the contacts Table
- * Testing the Contact Book’s Database

- At this point, we’ve created a PyQt application and its main window’s GUI to build our contact book project. In this section, we’ll write code to define how the application connects to the contact database. To complete this step, we’ll use SQLite to handle the database and PyQt’s SQL support to connect the application to the database and to work with our contact data.

![Contact Book Step 3](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Files/Contact%20Book%20Step%203.png)


Step 4: Displaying and Updating Existing Contacts

- * Creating a Model to Handle the Contact Data
- * Connecting the Model to the View
- * Displaying and Updating Contacts

-To display our contact data in the application’s main window, we can use QTableView. This class is part of PyQt’s Model-View architecture and provides a robust and efficient way of displaying items from a PyQt model object.

![Contact Book Step 3](https://github.com/Noob-Coders-2023/contact-book-project/blob/main/Files/Contact%20Book%20Step%204.png)


Step 5: Creating New Contacts

- * Creating the Add Contact Dialog
- * Launching the Add Contact Dialog
- * Processing the Add Dialog’s Data in the Model

- At this step, our contact book application provides functionality to load, display, and update the information about our contacts. Even though we’re able to modify and update the contact information, we can neither add nor remove contacts from the list.
In this section, we’ll provide the required functionality to add new contacts to the database, using a pop-up dialog to enter the new information.