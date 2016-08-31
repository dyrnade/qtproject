# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Aug 29 13:51:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide import QtSql

import sys

class DatabaseListModel(QtCore.QAbstractListModel):

    def __init__(self,items=[],parent=None):
        QtCore.QAbstractListModel.__init__(self,parent)
        self.__items = items

    def headerData(self,section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return "Orientation"
            else:
                return "Section %1".arg(section)


    def rowCount(self,parent):
        return len(self.__items)

    def data(self, index, role):

        row = index.row()
        value = self.__items[row]

        if role == QtCore.Qt.EditRole:
            return self.__items[row]

        if role == QtCore.Qt.DisplayRole:
            return value

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role = QtCore.Qt.EditRole):

        if role == QtCore.Qt.EditRole:

            row = index.row()
            if value:
                self.__items[row] = value
                self.dataChanged.emit(index,index)
                return True
        return False


app = QtGui.QApplication(sys.argv)
app.setStyle("plastique")

lview = QtGui.QListView()
lview.show()

items = DatabaseListModel(["131","asda","as","laskdas"])
lview.setModel(items)



app.exec_()

