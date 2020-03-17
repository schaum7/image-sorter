from PyQt5 import QtWidgets
from UI.mainwindow import Ui_ImageSorter
import ImageSorter
import os
import sys

app = QtWidgets.QApplication(sys.argv)


class ImageSorterMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImageSorter()
        self.ui.setupUi(self)
        self.setWindowTitle("ImageSorter")

        self.ui.btn_sortieren_starten.clicked.connect(
            self.on_btn_sortieren_starten_click)

    def on_btn_sortieren_starten_click(self):
        source_path = self.ui.le_path_source.text()
        target_path = self.ui.le_path_target.text()

        if source_path == "" or target_path == "":
            self.ui.lbl_result.setText(
                "FEHLER: einer der beiden Pfade ist leer!")
        else:
            self.ui.lbl_result.setText("sortiere...")
            ImageSorter.sort_images(source_path, target_path)
            self.ui.lbl_result.setText("Scheint funktioniert zu haben..")


window = ImageSorterMainWindow()
window.show()
sys.exit(app.exec_())


# gs8 = "C:\\Users\\falka\\Bilder\\Galaxy S8"
# desti_path = os.path.join(os.getcwd(), "target")
