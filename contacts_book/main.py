# Coding and Running the Application
# This module provides Contact Book application.

import sys
from PyQt5.QtWidgets import QApplication
from .views import Window

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

# 'import sys' imports the sys module, which provides access to
# various system-specific parameters and functions, including command-line arguments.

# 'from PyQt5.QtWidgets import QApplication' imports the QApplication class from the PyQt5.QtWidgets module.
# QApplication is an essential class in PyQt5 for managing the application's main event loop and overall initialization.

# 'from .views import Window' imports a class named Window from a module called views.
# The dot . before views indicates that it's a relative import,
# meaning that the views module is located in the same package or directory as the script.

# -------------------------------------------------------------------------------------

# [Contact Book main function.]
# 'def main()' defines a Python function named main().
# This function will serve as the entry point for running the application.

# [Create the application]
# 'app = QApplication(sys.argv)' creates an instance of the QApplication class,
# which represents the application itself.
# It takes sys.argv as an argument, which contains the command-line arguments passed to the script.
# QApplication is responsible for setting up the application's event loop and managing its behavior.

# [Create the main window]
# 'win = Window()' creates an instance of the Window class, which was imported earlier.
# This Window class represents the main window of the application.

# 'win.show()' calls the show() method on the win object.
# This method is used to display the main window on the screen.

# [Run the event loop]
# 'sys.exit(app.exec())' starts the application's event loop by calling the exec() method on the app object.
# The sys.exit() function is used to ensure that the application exits gracefully when the main window is closed
# by the user or when the application finishes its execution.

# -------------------------------------------------------------------------------------

# In summary, this code sets up the main entry point for a PyQt5-based GUI application.
# It creates an application instance, creates the main window, shows it on the screen, and starts the event loop,
# which allows the application to respond to user interactions and events.