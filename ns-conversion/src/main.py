import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from widgets.conversion_widget import ConversionWidget
from widgets.addition_widget import AdditionWidget
from widgets.encode_widget import EncodeWidget
from widgets.decode_widget import DecodeWidget

# Import styles from external file
from styles.styles import APP_STYLES

class NumberSystemApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number System Calculator")
        self.setGeometry(100, 100, 300, 600)
        
        # Set application style from external file
        self.setStyleSheet(APP_STYLES)
        
        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # Title
        title = QLabel("Number System Calculator")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #4CAF50; margin-bottom: 15px;")
        main_layout.addWidget(title)
        
        # Create widgets
        self.conversion_widget = ConversionWidget()
        self.addition_widget = AdditionWidget()
        self.encode_widget = EncodeWidget()
        self.decode_widget = DecodeWidget()
        
        # Connect encode widget to decode widget
        self.encode_widget.encoded.connect(self.decode_widget.set_encoded_data)
        
        # Add all widgets to main layout
        main_layout.addWidget(self.conversion_widget)
        main_layout.addWidget(self.addition_widget)
        main_layout.addWidget(self.encode_widget)
        main_layout.addWidget(self.decode_widget)
        
        # Initially show only the conversion widget
        self.hide_all_widgets()
        self.conversion_widget.setVisible(True)
        
        # Add menu buttons
        self.create_menu_buttons(main_layout)
        
    def create_menu_buttons(self, layout):
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        btn_convert = QPushButton("Conversion")
        btn_convert.setStyleSheet("QPushButton { background-color: #2196F3; } QPushButton:hover { background-color: #1e88e5; }")
        btn_convert.clicked.connect(lambda: self.show_widget(self.conversion_widget))
        
        btn_add = QPushButton("Addition")
        btn_add.setStyleSheet("QPushButton { background-color: #FF9800; } QPushButton:hover { background-color: #f57c00; }")
        btn_add.clicked.connect(lambda: self.show_widget(self.addition_widget))
        
        btn_encode = QPushButton("Encode")
        btn_encode.setStyleSheet("QPushButton { background-color: #9C27B0; } QPushButton:hover { background-color: #7b1fa2; }")
        btn_encode.clicked.connect(lambda: self.show_widget(self.encode_widget))
        
        btn_decode = QPushButton("Decode")
        btn_decode.setStyleSheet("QPushButton { background-color: #F44336; } QPushButton:hover { background-color: #d32f2f; }")
        btn_decode.clicked.connect(lambda: self.show_widget(self.decode_widget))
        
        button_layout.addWidget(btn_convert)
        button_layout.addWidget(btn_add)
        button_layout.addWidget(btn_encode)
        button_layout.addWidget(btn_decode)
        
        layout.addLayout(button_layout)
    
    def hide_all_widgets(self):
        self.conversion_widget.setVisible(False)
        self.addition_widget.setVisible(False)
        self.encode_widget.setVisible(False)
        self.decode_widget.setVisible(False)
    
    def show_widget(self, widget):
        self.hide_all_widgets()
        widget.setVisible(True)

def main():
    app = QApplication(sys.argv)
    window = NumberSystemApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    