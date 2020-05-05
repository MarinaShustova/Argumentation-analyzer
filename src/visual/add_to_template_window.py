from PyQt5 import QtWidgets, uic

class AddToTemplateWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui-files/create_templates.ui', self)
        # self.text = selected_text
        # self.initUI()

    # def initUi(self):
