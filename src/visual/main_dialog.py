import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from visual import templates_window
from visual import add_to_template_window

global library


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('../ui-files/text_edit_main.ui', self)
        self.initUI()

    def initUI(self):
        self.open_file.clicked.connect(self.show_dialog)
        self.templates_list.clicked.connect(self.show_library)
        self.add_to_template.clicked.connect(self.add_to_template_function)
        self.models.clicked.connect(self.show_models)
        self.setWindowTitle('Argument analyzer')

    def show_dialog(self):
        f_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        if f_name != '':
            f = open(f_name, 'r')
            try:
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
                    self.highlight_unions()
            except UnicodeDecodeError as ude:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("File is not UTF-encoded")
                msg.exec_()

    def highlight_unions(self):
        cursor = self.textEdit.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
        # Setup the regex engine
        pattern = "связано|Связано"
        regex = QtCore.QRegExp(pattern)
        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.textEdit.toPlainText(), pos)
        while (index != -1):
            # Select the matched text and apply the desired format
            cursor.setPosition(index)
            cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
            cursor.mergeCharFormat(format)
            # Move to the next match
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.textEdit.toPlainText(), pos)

    def add_to_template_function(self):
        self.thesis_window = add_to_template_window.AddToTemplateWindow()
        self.thesis_window.show()

    def show_library(self):
        self.templates = templates_window.TemplatesWindow()
        self.templates.show()

    def show_models(self):
        self.models = ModelsWindow()
        self.models.show()



# class ModelsWindow(QtWidgets.QDialog, modelsWindow.Ui_Dialog):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.tableWidget.setRowCount(len(library.models))
#         self.tableWidget.setColumnCount(2)
#         self.tableWidget.setHorizontalHeaderLabels(
#             ('Модель', 'Шаблон')
#         )
#         self.setWindowTitle('Модели')
#         self.fill_table()
#         self.set_compare_button()
#         self.set_show_button()
#
#     def set_compare_button(self):
#         self.compare.clicked.connect(self.show_comparison)
#
#     def set_show_button(self):
#         self.show_single.clicked.connect(self.show_model_info)
#
#     def show_model_info(self):
#         items = self.tableWidget.selectedItems()
#         length = len(items)
#         for i in range(length):
#             msg = QtWidgets.QMessageBox()
#             msg.setIcon(QtWidgets.QMessageBox.Information)
#             msg.setWindowTitle("Информация о модели")
#             msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
#             m = library.get_model_by_name(items[i].text())
#             msg.setText("Модель {}".format(m.get_name()))
#             msg.setDetailedText("Импликации модели:\n{}".format(self.cute_model_print(m)))
#             msg.exec_()
#
#     def cute_model_print(self, model):
#         a = ""
#         for impl in model.template.implications:
#             a += model.constants[impl.id][impl.left_expr] + " -> " + model.constants[impl.id][impl.right_expr] + "\n"
#         return a
#
#     def show_comparison(self):
#         items = self.tableWidget.selectedItems()
#         if len(items) != 2:
#             self.show_warn_dialog()
#         else:
#             model1 = library.get_model_by_name(items[0].text())
#             model2 = library.get_model_by_name(items[1].text())
#             self.describe_intersection(model1.compare(model2))
#
#     def describe_intersection(self, intersect):
#         msg = QtWidgets.QMessageBox()
#         msg.setIcon(QtWidgets.QMessageBox.Information)
#         msg.setWindowTitle("Результат сравнения")
#         msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
#         if intersect == False:
#             msg.setText("Эти модели независимы")
#             msg.setInformativeText("У шаблонов этих моделей нет ничего общего")
#             msg.exec_()
#         else:
#             msg.setText("У этих моделей есть потенциальные противоречия")
#             msg.setInformativeText("У этих моделей {} несовпадающих импликаций".format(len(intersect)))
#             msg.setDetailedText("Потенциальные противоречия:\n{}".format(self.cute_print(intersect)))
#             msg.exec_()
#
#     def cute_print(self, contradictions):
#         a = ""
#         for i in contradictions:
#             similarity = stat_similarity(i[1].split()[0], i[2].split()[0])
#             if similarity != 'Unknown' and float(similarity) >= 0.5:
#                 res = " [OK]\n"
#             else:
#                 res = " [WARN]\n"
#             a += i[0] + ": " + i[1] + " и " + i[2] + res
#         return a
#
#     def show_warn_dialog(self):
#         msg = QtWidgets.QMessageBox()
#         msg.setIcon(QtWidgets.QMessageBox.Warning)
#
#         msg.setText("Модели можно сравнивать только попарно!")
#         msg.setInformativeText("Пожалуйста, выберите две модели для сравнения")
#         msg.setWindowTitle("Предупреждение")
#         msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
#         msg.exec_()
#
#     def fill_table(self):
#         row = 0
#         for model in library.models:
#             cellinfo = QtWidgets.QTableWidgetItem(model.get_name())
#             self.tableWidget.setItem(row, 0, cellinfo)
#             cellinfo = QtWidgets.QTableWidgetItem(model.template.get_name())
#             self.tableWidget.setItem(row, 1, cellinfo)
#             row += 1


def run_windows():
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    print(sys.path)
    run_windows()
