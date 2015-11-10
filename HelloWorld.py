import sys
from PySide.QtCore import Qt
from PySide.QtGui import *


# Create the main application window
qt_app = QApplication(sys.argv)


class HelloWorld(QLabel):
    ''' A QT application that displays the text, "Hello World!" '''
    def __init__(self):
    # Initialize the object as a QLabel
        QLabel.__init__(self, "Hello World!")

        # Set the size, alignment and title
        self.setMinimumSize(600,400)
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Hello, World!")

    def run(self):
        ''' Show the application window and start the main loop event '''
        self.show()
        qt_app.exec_()


HelloWorld().run()

