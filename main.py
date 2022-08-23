import sys
from PyQt5.QtWidgets import *

def say_hello():
    print("Hello wolrd!")

app = QApplication(sys.argv)

with open("style.qss", 'r') as f:
    _style = f.read()
    app.setStyleSheet(_style)

#Main window widget
root = QWidget()
root.resize(800, 480)
root.setWindowTitle("PipBoyQt")
root.show()

#Main vertical box
mainVbox = QVBoxLayout(root)

#Top bar for time et settings button
topBar = QHBoxLayout()
mainVbox.addLayout(topBar)

#Date and hour display
hour = QLabel()
hour.setText("17.08.2022 17:08")
topBar.addWidget(hour)

#Space between the date andthe settings button
topBarSpacer = QSpacerItem(10, 0)
topBar.addSpacerItem(topBarSpacer)

#Settings button
settingsButton = QPushButton()
settingsButton.setText("Settings")
settingsButton.clicked.connect(say_hello)
topBar.addWidget(settingsButton)

#Radio tab
radioW = QWidget()
radioLayout = QGridLayout(radioW)
radioList = QListWidget()
radioList.addItems(["LFM", "One FM", "RTS"])
radioList.currentItemChanged.connect(say_hello)
radioLayout.addWidget(radioList, 0, 0, 3, 1)
radioFreq = QLabel("107.25")
radioLayout.addWidget(radioFreq, 0, 1, 1, 5)
radioPrevButton = QPushButton("F Prev")
radioLayout.addWidget(radioPrevButton, 1, 1)
radioPrevButton = QPushButton("Prev")
radioLayout.addWidget(radioPrevButton, 2, 2)
radioPlayButton = QPushButton("Play")
radioLayout.addWidget(radioPlayButton, 1, 3)
radioNextButton = QPushButton("Next")
radioLayout.addWidget(radioNextButton, 2, 4)
radioNextButton = QPushButton("F Next")
radioLayout.addWidget(radioNextButton, 1, 5)

#Navit maps tab
mapW = QWidget()

#Calendar tab
cal = QCalendarWidget()

#Remote tab
remoteW = QWidget()

#NFC tab
nfcW = QWidget()

#Wireless settings tab
wirelessW = QWidget()

#Monitor tab
monitorW = QWidget()

#Terminal tab
terminalW = QWidget()

#Tabs wigets
tabs = QTabWidget(root)
tabs.addTab(radioW, "Radio")
tabs.addTab(mapW, "Map")
tabs.addTab(cal, "Calendar")
tabs.addTab(remoteW, "Remote")
tabs.addTab(nfcW, "NFC")
tabs.addTab(wirelessW, "Wireless")
tabs.addTab(monitorW, "Monitor")
tabs.addTab(terminalW, "Terminal")
mainVbox.addWidget(tabs)

sys.exit(app.exec_())