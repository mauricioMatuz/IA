from PySide2.QtWidgets import QApplication
from Controller.Genetico import Genetic


if __name__ == "__main__":
    app = QApplication()
    window = Genetic()
    window.show()

    app.exec_()