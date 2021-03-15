from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Mytrewidget import *





class MytreeWidget(QtWidgets.QTreeWidget):

    def __init__(self,parent = None):
        QtWidgets.QTreeWidget.__init__(self , parent)
        #self.itemPressed.connect(self.expandItem)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.menuContextTree)
        #self.setHeaderHidden(True)
        self.setUniformRowHeights(True)
        self.setAllColumnsShowFocus(True)
        self.header().setCascadingSectionResizes(True)
        self.header().setStretchLastSection(True)



    def menuContextTree(self, point):
        count = self.topLevelItemCount()
        print(count)
        if count == 0:
            reply = QMessageBox.question(self, 'Пусто',
                                         "Добавить новую категорию?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                item_n = QtWidgets.QTreeWidgetItem(self)
                self.topLevelItem(0).setText(0, "новая категория")
        def editItem():
            item = self.currentItem()
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.editItem(item, 0)

        def addItem():


            item = QtWidgets.QTreeWidgetItem(self)
            item.setText(0, "новая категория")
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.addTopLevelItem(item)
            self.editItem(item, 0)

        def addItem_child():
            item = self.currentItem()
            ch = QtWidgets.QTreeWidgetItem(0)
            ch.setText(0, "новая подкатегория")
            ch.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            item.addChild(ch)
            self.editItem(ch, 0)
            self.expandItem(item)

        def deleteItem():
            item = self.currentItem()
            i = self.indexOfTopLevelItem(item)

            chCount = item.childCount()  # если есть доч. элементы
            if chCount > 0:
                reply = QMessageBox.question(self, 'Ошибка удаления',
                                             "Вы действительно хотите удалить и подкатегории?", QMessageBox.Yes |
                                             QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    if item.parent() is not None:
                        item.parent().removeChild(item)
                    else:
                        self.takeTopLevelItem(i)
                else:
                    return
            else:
                if item.parent() is not None:
                    item.parent().removeChild(item)
                else:
                    self.takeTopLevelItem(i)

        # --- меню----
        index = self.indexAt(point)
        if not index.isValid():
            return
        item = self.itemAt(point)
        name = item.text(0)  # The text of the node.itemAt(position)

        # We build the menu.
        menu = QtWidgets.QMenu()
        # action = menu.addAction(name)

        action_1 = menu.addAction("Редактировать")
        action_2 = menu.addAction("Новая категория")
        action_4 = menu.addAction("Новая подкатегория")
        menu.addSeparator()
        action_3 = menu.addAction("Удалить")

        action_1.triggered.connect(editItem)
        action_2.triggered.connect(addItem)
        action_3.triggered.connect(deleteItem)
        action_4.triggered.connect(addItem_child)
        menu.exec_(self.mapToGlobal(point))


    # def expandItem(self):
    #     print("press")


