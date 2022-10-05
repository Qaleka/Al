from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from PyQt6.QtWidgets import QApplication, QPushButton

import sys


def main():
    r = Rectangle("синего", 1, 3)
    c = Circle("зеленого", 1)
    s = Square("красного", 1)
    print(r)
    print(c)
    print(s)

    app = QApplication(sys.argv)
    window = QPushButton("Greetings everyone")
    window.show()
    app.exec()

if __name__ == "__main__":
    main()