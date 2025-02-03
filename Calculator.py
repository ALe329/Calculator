'''Калькулятор'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QComboBox, QCheckBox, QRadioButton, QLineEdit, QTextEdit, QTextBrowser, QSpinBox, QDoubleSpinBox, \
    QGroupBox, \
    QFormLayout, QCalendarWidget, QMenu, QToolBar, QSplitter, QTabWidget, QSlider,QGridLayout
from PyQt6.QtGui import QPalette, QColor, QAction, QPixmap
import sys

# Создаем класс кнопки

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        #Создаем основной вертикальный бокслэй
        self.osn_layout = QVBoxLayout()
        #Создаем лайнтекст для вывода данных
        self.line_text_1 = QLineEdit()
        self.osn_layout.addWidget(self.line_text_1)
        self.grid_lay=QGridLayout()
        self.osn_layout.addLayout(self.grid_lay)
        self.but_second_gor_lay()


        self.init_UI()

    def but_second_gor_lay(self):
        names_buttons=['AC','%','del','/','7','8','9','*','4','5','6','-','1','2','3','+','00','0','.','=']
        self.button_dict={}

        for j in range(int(len(names_buttons))):
            button=QPushButton(names_buttons[j])
            button.clicked.connect(self.button_clicked)
            self.button_dict[names_buttons[j]] = button
            self.grid_lay.addWidget(button, 1 + (j // 4), j % 4)



    # Получаем ссылку на кнопку, которая была нажата
    def button_clicked(self):
        button = self.sender().text()

        # Очищаем текстовое поле
        if button== 'AC':
            self.line_text_1.clear()
        elif button=='del':
        # Удаляем последний символ из текстового поля
            current_text=self.line_text_1.text()
            self.line_text_1.setText(current_text[:-1])
        elif button == '=':
            virazenie = self.line_text_1.text()
            result = eval(virazenie)  # Вычисляем выражение
            self.line_text_1.setText(str(result))  # Показываем результат
        else:
            current_text = self.line_text_1.text()
            self.line_text_1.setText(current_text + button)
    def init_UI(self):
        widget = QWidget()
        widget.setLayout(self.osn_layout)
        self.setCentralWidget(widget)
        self.setGeometry(200, 200, 450, 300)
        self.setWindowTitle("Супер-МОЩЩНЫЙ Калькулятор")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec())
