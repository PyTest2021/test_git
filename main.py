
from t2 import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def st_set0():
    ui.stackedWidget.setCurrentIndex(0)
    ui.label.setText("страница1")

def st_set1():
    ui.stackedWidget.setCurrentIndex(3)
    ui.label.setText("страница2")

def st_set2():
    ui.stackedWidget.setCurrentIndex(2)
    ui.label.setText("страница3")

def st_set3():
    ui.stackedWidget.setCurrentIndex(1)
    ui.label.setText("страница4")

def prepare_tool_buttons(ToolButton,icon):
    '''
    Функция настраивающая toolbutton для отображения иконок, эффективной визуализации кнопки с использованием qss
    при взаимодействии пользователя с кнопкой. Функция применяется к кнопке (ToolButton), также на вход подается
    путь к иконке (icon).
    '''
    # Вначале делаем общие настройки кнопки
    ToolButton.setAutoExclusive(True) #Если нажата одна кнопка у определенного родителя другие отжаты
    ToolButton.setCheckable(True) #Можно нажать и отпуустить кнопку
    ToolButton.setMinimumSize(80, 60) #Устанавливаем размер кнопки минимальный
    ToolButton.setMaximumSize(80, 60) #Устанавливаем размер кнопки максимальный
    ToolButton.setIcon(QIcon(icon))
    ToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    ToolButton.setIconSize(QtCore.QSize(40, 40))

    # ToolButton.setToolButtonStyle(QtGui.ToolButtonTextUnderIcon)

    # Настройка кнопок переключателей виджетов QStackedWidget(основное меню)
    # Задаем переключатели, как QToolButton и настраиваем их внешний вид

    # ------------------------Создаем стиль qss для отображения окна и кнопок, который будет включать:-----------------
    # 1)Заливку основного фона делаем ее градиентом из нижнего левого в верхний правый
    # 2)Удаляем рамку кнопки и ставим прозрачным фоновую заливку кнопки
    # 3)Добавляем стиль если кнопка включена
    # 4)Добавляем стиль взаимодействия когда стрелка мышки проходит над кнопкой

    style = '''
    QToolButton {background-color: transparent;
                 border: none}
    QToolButton::hover {background-color: rgb(224, 232, 246)}
    QToolButton::checked {background-color: rgb(139, 210, 238);
                          border: 1px solid rgb(60, 127, 177)}
    '''
    ToolButton.setStyleSheet(style)

prepare_tool_buttons(ui.toolButton,icon= '.\icons\well_icon.png')
prepare_tool_buttons(ui.toolButton_2,icon= '.\icons\well_icon.png')
prepare_tool_buttons(ui.toolButton_3,icon= '.\icons\well_icon.png')
prepare_tool_buttons(ui.toolButton_4,icon= '.\icons\well_icon.png')

#
# ui.toolButton.setText("первая")
# setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
# icon = QtGui.QIcon()
# icon.addPixmap(QtGui.QPixmap("../icons/palitrra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
# self.choose_file_button.setIcon(icon)
# self.toolButton_clear_curent.setIconSize(QtCore.QSize(30, 30))
#
ui.toolButton.clicked.connect(st_set0)
ui.toolButton_2.clicked.connect(st_set1)
ui.toolButton_3.clicked.connect(st_set2)
ui.toolButton_4.clicked.connect(st_set3)

sys.exit(app.exec_())
# чтото доб