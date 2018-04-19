import sys
import os
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,QHBoxLayout,
							QStackedLayout,QPushButton,QLabel,QTabBar,
							QLineEdit,QFrame,QTabWidget)

from PyQt5.QtGui import QIcon,QWindow,QImage
from PyQt5.QtWebEngineWidgets import *

class addressBar(QLineEdit):
	def __init__(self):
		super().__init__()

	def mousePressEvent(self,e):
		self.selectAll()

#main class
class App(QFrame):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Web browser")
		self.setBaseSize(1366,768)
		self.create_app()

	def create_app(self):
		#main layout
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)

		#tag
		self.qtbar = QTabBar(movable=True,tabsClosable=True)

		self.qtbar.tabCloseRequested.connect(self.closeTab)

		#tag plus
		self.addButton = QPushButton("+")
		self.addButton.clicked.connect(self.addtag)

		#addressbar -> search bar
		self.addressbar = addressBar()

		self.toolbar = QWidget()
		self.toolbarLayout = QHBoxLayout()
		self.toolbar.setLayout(self.toolbarLayout)
		self.toolbarLayout.addWidget(self.addressbar)
		self.toolbarLayout.addWidget(self.addButton)

		#To store tab and its content
		self.container = QWidget()
		self.container.layout = QStackedLayout()
		self.container.setLayout(self.container.layout)

		#show the main app's image
		self.layout.addWidget(self.qtbar)
		self.layout.addWidget(self.toolbar)
		self.layout.addWidget(self.container)

		#record the tag
		self.tagcount = 0
		self.tagObject = []

		#initialize first tag
		self.addtag()

		self.setLayout(self.layout)

		self.show()

	def closeTab(self,i):
		self.qtbar.removeTab(i)

	def addtag(self):
		i = self.tagcount

		#one tab, one content -> a layout
		self.tagObject.append(QWidget())
		self.tagObject[i].layout = QVBoxLayout()
		self.tagObject[i].setObjectName("tabs"+str(i))

		#get content from website that you want to browse
		self.tagObject[i].content = QWebEngineView()
		self.tagObject[i].content.load(QUrl.fromUserInput("https://www.google.com"))

		self.tagObject[i].layout.addWidget(self.tagObject[i].content)

		self.tagObject[i].setLayout(self.tagObject[i].layout)

		#store this tag to container, that will help to keep content and avoid to be lost
		self.container.layout.addWidget(self.tagObject[i])
		self.container.layout.setCurrentWidget(self.tagObject[i])

		self.qtbar.addTab("New tab")

		self.tagcount+=1

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = App()

	sys.exit(app.exec_())

