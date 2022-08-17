import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QWindow

def say_hello():
    print("Hello wolrd!")

app = QApplication(sys.argv)

win = QWidget()
winID = int(win.winId())

sub_win = QWindow.fromWinId(winID)
container = QWidget.createWindowContainer(sub_win)
sub_win_id = int(container.winId())

process = QProcess(container)
process.start("navit")

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
settingsButton.setText("Click me!")
settingsButton.clicked.connect(say_hello)
topBar.addWidget(settingsButton)

#Radio tab
radioW = QWidget()
radio1 = QPushButton("Radio 1", radioW)
radio2 = QPushButton("Radio 2", radioW)

#Navit maps tab


#Calendar tab
cal = QCalendarWidget()

#Tabs wigets
tabs = QTabWidget(root)
tabs.addTab(radioW, "Radio")
tabs.addTab(container, "Map")
tabs.addTab(cal, "Calendar")
mainVbox.addWidget(tabs)

sys.exit(app.exec_())