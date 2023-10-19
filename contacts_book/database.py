# Connecting to the Database With PyQt and SQLite
# This module provides a database connection.

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuerye.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )

        """
    )


def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("ContactBookDB")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Contact Book",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()
    return True

# 'QSqlQuery' to execute and manipulate SQL statements.

# 'connection = QSqlDatabase.addDatabase("ContactBookDB")' creates the database connection using the QSQLITE driver.

# 'connection.setDatabaseName(ContactBookDB)' sets the filename or the path to the database.

# 'if not connection.open():' attempts to open the connection. If a problem occurs during the call to .open(),
# then the if code block shows an error message and then returns False to indicate that the connection attempt failed.

# 'return True' returns True if the connection attempt is successful.
