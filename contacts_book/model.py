# Creating a Model to Handle the Contact Data
# This module provides a model to manage the contacts table.

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()
    

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel


    def addContact(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()

    
    def deleteContact(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    
    def clearContacts(self):
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

# 'self.model = self._createModel()' define an instance attribute called .model to hold the data model.

# 'tableModel = QSqlTableModel()' creates an instance of QSqlTableModel() called tableModel.

# 'tableModel.setTable("contacts")' associates the model object with the contacts table in your database.

# 'tableModel.setEditStrategy(QSqlTableModel.OnFeildChange)' sets the .editStrategy property of the model to QSqlTableModel.OnFieldChange.
# With this, you ensure that the changes on the model get saved into the database immediately.

# 'tableModel.select()' loads the table into the model by calling .select().

# 'headers = ("ID", "Name", "Job", "Email")'
# for columnIndex, header in enumerate(headers):'                  :define and set user-friendly headers for the contacts table’s columns. 
# tableModel.setHeaderData(columnIndex, Qt.horizontal, header)'

# 'return tableModel' returns the newly created model.

# 'rows = self.model.rowCount()' gets the current number of rows in the data model.

# 'self.model.insertRows(rows, 1)' inserts a new row at the end of the data model.

# 'for column, field in enumerate(data):
# self.model.setData(self.model.index(rows, column + 1), field)' run a for loop that inserts every item in data into the corresponding cell in the data model.
# To do this, line 9 calls .setData() on the model, with the index of the cell and the current data field as arguments.

# 'self.model.submitAll()' submits the changes to the database by calling .submitAll() on the model.

# 'self.model.select()' reloads the data from the database into the model.

# 'def deleteContact(self, row):' remove a contact from the database.

# 'self.model.removeRow(row)' removes the selected row.

# 'self.model.submitAll()' submits the change to the database.

# 'self.model.select()' reloads the data into the model.

# 'def clearContacts(self):' remove all contacts in the database.

# 'self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)' allows us to cache all the changes until we call .submitAll() later on.
# We need to do this because we’re changing several rows at the same time.

# 'self.model.removeRows(0, self.model.rowCount())' removes all the rows from the model.

# 'self.model.submitAll()' saves changes to the database.

# 'self.model.setEditStrategy(QSqlTableModel.OnFieldChange)' resets the model’s .editStrategy property to its original value, QSqlTableModel.OnFieldChange.
# If we don’t reset this property to its original value, then we won’t be able to update the contacts directly in the table view.

# 'self.model.select()' reloads the data into the model.