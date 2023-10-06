from subprocess import run
import sys
from PyQt5 import QtWidgets
from UI import Ui_Form


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def choose_path(self):
        filePath = QtWidgets.QFileDialog.getExistingDirectory()
        filePath = "".join(filePath)
        self.label.setText('"' + filePath + '"')

    def format1_change(self, text):
        self.lineEdit.setText(text)

    def format2_change(self, text):
        self.lineEdit_2.setText(text)

    def rename(self):
        name = self.lineEdit_3.text()
        format1 = self.lineEdit.text()
        format2 = self.lineEdit_2.text()
        path = self.label.text()
        commond_cd = '"cd ' + path
        commond = (
            "Get-ChildItem *."
            + format1
            + ' | ForEach-Object -Begin {;\
        $count = 1;\
        } -Process {;\
        Rename-Item $_ -NewName \\"'
            + name
            + "$count."
            + format2
            + '\\";\
        $count++ ;\
        }'
        )
        commond = str(commond)
        run("powershell " + commond_cd + ";" + commond + '"', shell=True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.setWindowTitle("Rename")
    ui.show()
    sys.exit(app.exec_())
