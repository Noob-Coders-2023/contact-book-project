# Creating the Application’s Main Window
# This module provides views to manage the contacts table.

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from .model import ContactsModel


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Contact Book")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")

        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("Job:", self.jobField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)

        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        super().accept()


# 'from PyQt5.QtWidgets import' is importing classes and functions from the PyQt5.QtWidgets module,
# which is a module within the PyQt5 library
# that provides tools and components for creating GUI applications.

# 'from .model import ContactsModel' import ContactsModel from model.py.

# 'QAbstractItemView' to provide access to the table view selection behavior policy.

# 'QHBoxLayout' is a class in PyQt5 that represents a horizontal layout.
# Layouts are used in GUI development to arrange widgets
# (such as buttons, labels, or other GUI elements) within a window or dialog in a specific way.

# 'QMainWindow' is a class in PyQt5 that represents the main application window.
# It provides a framework for building GUI applications with a menu bar, toolbar, and central widget area.

# 'QPushButton' to create the Add, Delete, and Clear All buttons.

# 'QTableView' to provide the table-like view that displays the contacts list.

# 'QWidget' is a fundamental class in PyQt5 that represents a generic widget.
# Widgets are the basic building blocks of GUI applications in PyQt5, and they can be used to create various UI elements.

# With this code, these classes are being imported,
# which means you can use them in your code to create and manage GUI elements and layouts when building a PyQt5 application.

# -------------------------------------------------------------------------------------

# 'class Window(QMainWindow)' defines a new class named Window that inherits from the QMainWindow class.

# 'def __init__(self, parent=None)' defines the constructor (__init__ method) for the Window class.
# It takes an optional parent argument, which is typically used to specify the parent widget of this widget.

# 'super().__init__(parent)' calls the constructor of the parent class (QMainWindow) and passes the parent argument to it.
# This ensures that the initialization code of QMainWindow is executed before any additional initialization specific to the Window class.

# self.setWindowTitle("Contact Book") sets the window's title to "Contact Book"

# self.resize(550, 250) sets the initial size of the window to a width of 550 pixels and a height of 250 pixels.


# self.centralWidget = QWidget() creates a central widget for the main window.
# The central widget is where you typically place other widgets and layout managers to build the user interface of your application.


# self.setCentralWidget(self.centralWidget) sets the central widget for the main window to the one created above.
# This means that any widgets or layouts you add to this centralWidget will be displayed in the main window.


# self.layout = QHBoxLayout() creates a horizontal layout (QHBoxLayout) and assigns it to the self.layout attribute of the Window instance.
# Layouts are used to arrange widgets within a window or container.


# self.centralWidget.setLayout(self.layout) sets the layout of the central widget to the horizontal layout created earlier.
# This means that any widgets added to this layout will be horizontally arranged within the central widget.

# 'self.addButton.clicked.connect(self.openAddDialog)' connects the .clicked() signal of the Add button to the newly created slot, .openAddDialog().
# This way, a click on the button will automatically call the slot.

# 'def openAddDialog(self):' defines the .openAddDialog() slot.

    # 'dialog = AddDialog(self)' creates an instance of AddDialog.

    # if dialog.exec() == QDialog.Accepted:
    #     self.contactsModel.addContact(dialog.data)
    #     self.table.resizeColumnsToContents()'

# -------------------------------------------------------------------------------------

# 'class AddDialog(QDialog):' defines a new class that inherits from QDialog.

# 'def __init__(self, parent=None): ...' define the class initializer.
# 'self.data = None'  is an instance attribute that you’ll use to hold the data your users provide.

# 'def setupUI(self):
        # self.nameField = QLineEdit()
        # self.nameField.setObjectName("Name") ...'  add three QLineEdit objects: name, job, and email.
        # We’ll use these line edits to take the user’s input for the name, job description, and email of the contact to add.
        # They represent the corresponding fields in the database.

        # layout = QFormLayout()
        # layout.addRow("Name:", self.nameField) ...' create a QFormLayout instance that arranges the line edits in a form.
        # This layout manager also provides user-friendly labels for each line edit or field.

        # self.buttonsBox = QDialogButtonBox(self)
        # self.buttonsBox.setOrientation(Qt.Horizontal)
        # self.buttonsBox.setStandardButtons(
        #     QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        # )' add a QDialogButtonBox object that provides two standard buttons: OK and Cancel.
        # The OK button accepts the user’s input and the Cancel button rejects it.

        # self.buttonsBox.accepted.connect(self.accept)
        # self.buttonsBox.rejected.connect(self.reject)' connect the dialog’s built-in .accepted() and .rejected() signals with the .accept() and reject() slots, respectively.
        # In this case, we’ll rely on the dialog’s built-in .reject() slot, which closes the dialog without processing the input.
        # Other than that, we just need to code the .accept() slot.


# 'def accept(self):' accept the data provided through the dialog.

    # 'self.data = []' initializes .data to an empty list ([]). This list will store the user’s input data.

    # 'for field in (self.nameField, self.jobField, self.emailField):' defines a for loop that iterates over the three line edits, or fields, in the dialog.

        # if not field.text():
        # QMessageBox.critical(
        #     self,
        #     "Error!",
        #     f"You must provide a contact's {field.objectName()}",
        # )
        # self.data = None  # Reset .data
        # # return' define a conditional statement that checks if the user has provided data for each field in the dialog. If not, then the dialog shows an error message that warns the user about the missing data.

    # 'self.data.append(field.text())' adds the user’s input for each field to .data.

    # 'super().accept()' calls the superclass’s .accept() slot to provide the standard behavior that closes the dialog after the user clicks OK.

# -------------------------------------------------------------------------------------

# Overall, these lines of code set up the main window for a PyQt5 application, including its title, size, central widget, and layout.
# You can add more widgets and customize the user interface further within this window class to create your application.
