import sys
from PyQt5.QtWidgets import *

def say_hello():
    print("Hello wolrd!")

app = QApplication(sys.argv)

with open("style.qss", 'r') as f:
    _style = f.read()
    app.setStyleSheet(_style)

root = QWidget()
root.resize(800, 480)
root.setWindowTitle("PipBoyQt")
root.show()

'''hour = QLabel(root)
hour.setText("17.08.2022 17:08")
hour.show()'''

'''button = QPushButton(root)
button.setText("Click me!")
button.clicked.connect(say_hello)
button.show()'''

'''tabs = QTabBar(root)
tabs.addTab("Radio")
tabs.addTab("Map")
tabs.addTab("Calendar")
tabs.show()'''

radioW = QWidget()
radio1 = QPushButton("Radio 1", radioW)
radio2 = QPushButton("Radio 2", radioW)

cal = QCalendarWidget()

tabs = QTabWidget(root)
tabs.addTab(radioW, "Radio")
#tabs.addTab("Map")
tabs.addTab(cal, "Calendar")
tabs.show()

sys.exit(app.exec_())