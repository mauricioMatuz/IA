from PySide2.QtWidgets import QApplication
from Controller.controller import Neurona


if __name__ == "__main__":
    app = QApplication()
    window = Neurona()
    window.show()

    app.exec_()