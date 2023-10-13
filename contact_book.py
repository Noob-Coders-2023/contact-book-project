# Coding and Running the Application
# This module provides RP Contacts entry point script.

from contacts_book.main import main

if __name__ == "__main__":
    main()


# 'from contacts_book.main import 'main' imports the main function from the 'main' module within the 'contacts_book' package or directory.
# The 'main' function is the entry point for application.

# 'if __name__ == "__main__"' is a conditional statement that checks whether the script is being run as the main program
# or if it's being imported as a module into another script.
# The '__name__' variable in Python is set to '"__main__"' when the script is executed directly.

# 'main()' calls the 'main()' function.
# It is executed only if the condition 'if __name__ == "__main__":' is true,
# indicating that the script is being run as the main program.

# -------------------------------------------------------------------------------------

# In summary, these lines of code are used to structure your Python script in such a way
# that the main() function is executed when the script is run directly but not when it's imported as a module into another script.
# This pattern allows you to create reusable and modular code while ensuring that the main entry point of your application is correctly invoked when you run the script directly.