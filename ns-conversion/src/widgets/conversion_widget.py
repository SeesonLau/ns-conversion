from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit)
from PyQt5.QtCore import QSize

from utils.conversion import decimal_to_all_bases

class ConversionWidget(QGroupBox):
    def __init__(self):
        super().__init__("Decimal to All Bases Conversion")
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Input
        input_layout = QHBoxLayout()
        input_label = QLabel("Decimal Number:")
        input_label.setFixedWidth(120)
        input_layout.addWidget(input_label)
        self.decimal_input = QLineEdit()
        self.decimal_input.setPlaceholderText("Enter decimal number")
        input_layout.addWidget(self.decimal_input)
        layout.addLayout(input_layout)
        
        # Convert button
        convert_btn = QPushButton("Convert")
        convert_btn.clicked.connect(self.convert_number)
        convert_btn.setStyleSheet("QPushButton { background-color: #2196F3; } QPushButton:hover { background-color: #1e88e5; }")
        layout.addWidget(convert_btn)
        
        # Result display
        result_layout = QVBoxLayout()
        result_label = QLabel("Conversion Results:")
        result_layout.addWidget(result_label)
        
        self.binary_result = QTextEdit()
        self.binary_result.setReadOnly(True)
        self.binary_result.setPlaceholderText("Binary result will appear here")
        self.binary_result.setMaximumHeight(30)
        result_layout.addWidget(QLabel("Binary:"))
        result_layout.addWidget(self.binary_result)
        
        self.octal_result = QTextEdit()
        self.octal_result.setReadOnly(True)
        self.octal_result.setPlaceholderText("Octal result will appear here")
        self.octal_result.setMaximumHeight(30)
        result_layout.addWidget(QLabel("Octal:"))
        result_layout.addWidget(self.octal_result)
        
        self.hex_result = QTextEdit()
        self.hex_result.setReadOnly(True)
        self.hex_result.setPlaceholderText("Hexadecimal result will appear here")
        self.hex_result.setMaximumHeight(30)
        result_layout.addWidget(QLabel("Hexadecimal:"))
        result_layout.addWidget(self.hex_result)
        
        layout.addLayout(result_layout)
        
        self.setLayout(layout)
    
    def convert_number(self):
        try:
            decimal_value = self.decimal_input.text()
            binary, octal, hexadecimal = decimal_to_all_bases(decimal_value)
            
            self.binary_result.setPlainText(binary)
            self.octal_result.setPlainText(octal)
            self.hex_result.setPlainText(hexadecimal)
            
            # Adjust height based on content
            self.adjust_text_edit_height(self.binary_result)
            self.adjust_text_edit_height(self.octal_result)
            self.adjust_text_edit_height(self.hex_result)
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))
    
    def adjust_text_edit_height(self, text_edit):
        # Calculate required height based on content
        doc = text_edit.document()
        doc.setTextWidth(text_edit.viewport().width())
        height = doc.size().height() + 10
        
        # Set minimum height and expand if needed
        text_edit.setMinimumHeight(30)
        if height > 30:
            text_edit.setMinimumHeight(int(height))
            