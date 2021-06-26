# # # # # # import sys
# # # # # # from PyQt5.QtCore import *
# # # # # # from PyQt5.QtGui import *
# # # # # # from PyQt5.QtWidgets import *
# # # # # # def window():
# # # # # #    app = QApplication(sys.argv)
# # # # # #    w = QWidget() ## Cửa sổ
# # # # # #    b = QLabel(w) ## Nhãn
# # # # # #    b.setText("Chào Việt Nam!")
# # # # # #    w.setGeometry(100,100,200,50) ## Thiet lap cua so
# # # # # #    b.move(50,20)
# # # # # #    w.setWindowTitle("Hệ chương trình quản lý bóng đá, 2021")
# # # # # #    w.show()
# # # # # #    sys.exit(app.exec_())
# # # # # # if __name__ == '__main__':
# # # # # #    window() ## Loi goi ham
# # # # #
# # # # # import sys
# # # # # from PyQt5.QtWidgets import *
# # # # # from PyQt5.QtGui import QFont
# # # # #
# # # # # class GridDemo(QWidget):
# # # # #     def __init__(self):
# # # # #         super().__init__()
# # # # #         global positions, values, position, value
# # # # #         values = ['Edit', 'Q&A', 'Biểu đồ', 'Trợ giúp']
# # # # #
# # # # #         positions = [(r, c) for r in range(3) for c in range(3)]
# # # # #
# # # # #
# # # # #         # print(self.rect().width()) # 80 times
# # # # #         layoutGrid = QGridLayout()
# # # # #         self.setLayout(layoutGrid)
# # # # #         self.buttons = {}
# # # # #
# # # # #         for position, value in zip(positions, values):
# # # # #             # print('Coordinate: ' + str(positions) + ' with value of '+ str(value))
# # # # #             self.buttons[position[0], position[1]] = QPushButton(value)
# # # # #             self.buttons[position[0], position[1]].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
# # # # #             self.buttons[position[0], position[1]].resizeEvent = self.resizeText
# # # # #             layoutGrid.addWidget(self.buttons[position[0], position[1]], *position) # widget, position --> row index, column index
# # # # #
# # # # #     def resizeText(self, event):
# # # # #         defaultSize = 9
# # # # #         # print(self.rect().width() // 1)
# # # # #         for position, value in zip(positions, values):
# # # # #             if self.rect().width() // 50 > defaultSize:
# # # # #                 f = QFont('', self.rect().width() // 50)
# # # # #             else:
# # # # #                 f = QFont('', defaultSize)
# # # # #             self.buttons[position[0], position[1]].setFont(f)
# # # # #
# # # # #
# # # # # def main():
# # # # #     app = QApplication(sys.argv)
# # # # #     demo = GridDemo()
# # # # #     demo.setWindowTitle("Chương trình Quản lý Bóng đá - CopyRight 2021")
# # # # #     demo.show()
# # # # #     sys.exit(app.exec_())
# # # # #
# # # # # main()
# # # #
# # # # # importing libraries
# # # # from PyQt5.QtWidgets import *
# # # # from PyQt5 import QtCore, QtGui
# # # # from PyQt5.QtGui import *
# # # # from PyQt5.QtCore import *
# # # # import sys
# # # #
# # # #
# # # # class Window(QMainWindow):
# # # #
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #
# # # #         # setting title
# # # #         self.setWindowTitle("Python ")
# # # #
# # # #         # setting geometry
# # # #         self.setGeometry(100, 100, 500, 400)
# # # #
# # # #         # calling method
# # # #         self.UiComponents()
# # # #
# # # #         # showing all the widgets
# # # #         self.show()
# # # #
# # # #     # method for components
# # # #     def UiComponents(self):
# # # #         # creating a QDateEdit widget
# # # #         date = QDateEdit(self)
# # # #
# # # #         # setting geometry of the date edit
# # # #         date.setGeometry(100, 100, 150, 40)
# # # #
# # # #         # date time
# # # #         d = QDateTime(2020, 10, 10, 10, 20)
# # # #
# # # #         # setting date time
# # # #         date.setDateTime(d)
# # # #
# # # #
# # # # # create pyqt5 app
# # # # App = QApplication(sys.argv)
# # # #
# # # # # create the instance of our Window
# # # # window = Window()
# # # #
# # # # # start the app
# # # # sys.exit(App.exec())
# # # from PyQt5 import QtCore, QtGui, QtWidgets
# # #
# # #
# # # class Ui_MainWindow(object):
# # #     def setupUi(self, MainWindow):
# # #         MainWindow.setObjectName("MainWindow")
# # #         MainWindow.resize(800, 600)
# # #         self.centralwidget = QtWidgets.QWidget(MainWindow)
# # #         self.centralwidget.setObjectName("centralwidget")
# # #         self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
# # #         self.verticalLayout.setObjectName("verticalLayout")
# # #         self.frame_2 = QtWidgets.QFrame(self.centralwidget)
# # #         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
# # #         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
# # #         self.frame_2.setObjectName("frame_2")
# # #         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
# # #         self.verticalLayout_2.setObjectName("verticalLayout_2")
# # #         self.frame = QtWidgets.QFrame(self.frame_2)
# # #         self.frame.setStyleSheet("background-color: rgb(56, 122, 179);")
# # #         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
# # #         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
# # #         self.frame.setObjectName("frame")
# # #         self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
# # #         self.horizontalLayout.setObjectName("horizontalLayout")
# # #         self.label = QtWidgets.QLabel(self.frame)
# # #         self.label.setStyleSheet("color: rgb(243, 243, 243);")
# # #         self.label.setObjectName("label")
# # #         self.horizontalLayout.addWidget(self.label)
# # #         self.dateEdit = QtWidgets.QDateEdit(self.frame)
# # #         self.dateEdit.setObjectName("dateEdit")
# # #         self.horizontalLayout.addWidget(self.dateEdit)
# # #         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
# # #         self.horizontalLayout.addItem(spacerItem)
# # #         self.verticalLayout_2.addWidget(self.frame)
# # #         self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
# # #         self.tableWidget.setObjectName("tableWidget")
# # #         self.tableWidget.setColumnCount(0)
# # #         self.tableWidget.setRowCount(0)
# # #         self.verticalLayout_2.addWidget(self.tableWidget)
# # #         self.verticalLayout.addWidget(self.frame_2)
# # #         MainWindow.setCentralWidget(self.centralwidget)
# # #
# # #         self.retranslateUi(MainWindow)
# # #         QtCore.QMetaObject.connectSlotsByName(MainWindow)
# # #
# # #     def retranslateUi(self, MainWindow):
# # #         _translate = QtCore.QCoreApplication.translate
# # #         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
# # #         self.label.setText(_translate("MainWindow", "Selected Date is :________________________"))
# # #
# # #
# # # if __name__ == "__main__":
# # #     import sys
# # #     app = QtWidgets.QApplication(sys.argv)
# # #     MainWindow = QtWidgets.QMainWindow()
# # #     ui = Ui_MainWindow()
# # #     ui.setupUi(MainWindow)
# # #     MainWindow.show()
# # #     sys.exit(app.exec_())
# # import sys
# # from PyQt4 import QtGui
# #
# # class Example(QtGui.QWidget):
# #
# #     def __init__(self):
# #         super(Example, self).__init__()
# #         self.initUI()
# #
# #     def initUI(self):
# #
# #         title = QtGui.QPushButton( 'Title' )
# #         author = QtGui.QPushButton( 'Author' )
# #         other = QtGui.QPushButton( 'Other' )
# #
# #         titleEdit = QtGui.QTextEdit()
# #
# #         horizontalLayout = QtGui.QHBoxLayout()
# #         horizontalLayout.addWidget( title )
# #         horizontalLayout.addWidget( author )
# #         horizontalLayout.addWidget( other )
# #
# #         verticalLayout = QtGui.QVBoxLayout( self )
# #         verticalLayout.addLayout( horizontalLayout )
# #
# #         verticalLayout.addWidget( titleEdit )
# #
# #
# #         self.setLayout( verticalLayout )
# #
# #         self.setGeometry( 300, 300, 350, 300 )
# #         self.setWindowTitle( 'Review' )
# #         self.show()
# #
# # def main():
# #
# #     app = QtGui.QApplication( sys.argv )
# #     ex = Example()
# #     sys.exit( app.exec_() )
# #
# #
# # if __name__ == '__main__':
# #     main()
#
# """
# ZetCode PyQt5 tutorial
#
# In this example, we position two push
# buttons in the bottom-right corner
# of the window.
#
# Author: Jan Bodnar
# Website: zetcode.com
# """
#
# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton,
#                              QHBoxLayout, QVBoxLayout, QApplication)
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(100)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Buttons')
#         self.show()
#
#
# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir, Qt


class DialogApp(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(800, 600)

		self.button1 = QPushButton('Upload image')
		self.button1.clicked.connect(self.get_image_file)

		self.button2 = QPushButton('Import Python Script')
		self.button2.clicked.connect(self.get_text_file)

		self.labelImage = QLabel()
		self.textEditor = QTextEdit()

		layout = QVBoxLayout()
		layout.addWidget(self.button1)
		layout.addWidget(self.labelImage, alignment=Qt.AlignCenter)
		layout.addWidget(self.button2)
		layout.addWidget(self.textEditor)
		self.setLayout(layout)

	def get_image_file(self):
		file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif)")
		self.labelImage.setPixmap(QPixmap(file_name))

	def get_text_file(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.AnyFile)
		dialog.setFilter(QDir.Files)

		if dialog.exec_():
			file_name = dialog.selectedFiles()

			if file_name[0].endswith('.py'):
				with open(file_name[0], 'r') as f:
					data = f.read()
					self.textEditor.setPlainText(data)
					f.close()
			else:
				pass

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = DialogApp()
	demo.show()

	sys.exit(app.exec_())