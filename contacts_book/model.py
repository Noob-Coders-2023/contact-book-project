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

