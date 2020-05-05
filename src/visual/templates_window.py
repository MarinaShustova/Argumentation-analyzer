from PyQt5 import QtWidgets, uic
from templates_service import TemplatesService


class TemplatesWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui-files/templates.ui', self)
        self.fill_list()
        self.setWindowTitle('Шаблоны')
        # self.set_compare_button()
        # self.set_show_button()

    # def set_compare_button(self):
    #     self.pushButton.clicked.connect(self.show_comparison)
    #
    # def set_show_button(self):
    #     self.pushButton_2.clicked.connect(self.show_template_info)
    #
    # def show_template_info(self):
    #     items = self.listWidget.selectedItems()
    #     length = len(items)
    #     for i in range(length):
    #         msg = QtWidgets.QMessageBox()
    #         msg.setIcon(QtWidgets.QMessageBox.Information)
    #         msg.setWindowTitle("Информация о шаблоне")
    #         msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #         t = library.get_template_by_name(items[i].text())
    #         msg.setText("Шаблон {}".format(t.get_name()))
    #         msg.setDetailedText("Импликации шаблона:\n{}".format(self.cute_print(t.implications)))
    #         msg.exec_()
    #
    # def show_comparison(self):
    #     items = self.listWidget.selectedItems()
    #     if len(items) != 2:
    #         self.show_warn_dialog()
    #     else:
    #         templ1 = library.get_template_by_name(items[0].text())
    #         templ2 = library.get_template_by_name(items[1].text())
    #         self.describe_intersection(templ1.compare(templ2))
    #
    # def describe_intersection(self, intersect):
    #     msg = QtWidgets.QMessageBox()
    #     msg.setIcon(QtWidgets.QMessageBox.Information)
    #     msg.setWindowTitle("Результат сравнения")
    #     msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #     if len(intersect) == 0:
    #         msg.setText("Эти шаблоны независимы")
    #         msg.setInformativeText("У шаблонов нет совпадающих импликаций")
    #         msg.exec_()
    #     else:
    #         msg.setText("Один шаблон расширяет другой")
    #         msg.setInformativeText("У этих шаблонов {} совпадающих импликаций".format(len(intersect)))
    #         msg.setDetailedText("Совпадающие импликации:\n{}".format(self.cute_print(intersect)))
    #         msg.exec_()
    #
    # def cute_print(self, implications):
    #     a = ""
    #     for i in implications:
    #         a += i.left_expr + " -> " + i.right_expr + "\n"
    #     return a
    #
    # def show_warn_dialog(self):
    #     msg = QtWidgets.QMessageBox()
    #     msg.setIcon(QtWidgets.QMessageBox.Warning)
    #
    #     msg.setText("Шаблоны можно сравнивать только попарно!")
    #     msg.setInformativeText("Пожалуйста, выберите два шаблона для сравнения")
    #     msg.setWindowTitle("Предупреждение")
    #     msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #     msg.exec_()

    def fill_list(self):
        t_serv = TemplatesService.TemplatesService()
        templates = t_serv.get_templates()
        for template in templates:
            self.listWidget.addItem(template.name)
