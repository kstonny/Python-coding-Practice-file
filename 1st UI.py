from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        btn = QPushButton("Hello Tony!", self)
        btn.move(100, 155)
        self.setGeometry(500, 500, 600, 350)
        self.setWindowTitle('PyQt Window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())