from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QTextEdit)

from utils.addition import add_numbers

class AdditionWidget(QGroupBox):
    def __init__(self):
        super().__init__("Add Numbers in Different Bases")
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # First number
        num1_layout = QHBoxLayout()
        num1_label = QLabel("First Number:")
        num1_label.setFixedWidth(100)
        num1_layout.addWidget(num1_label)
        self.add_num1 = QLineEdit()
        self.add_num1.setPlaceholderText("Enter first number")
        num1_layout.addWidget(self.add_num1)
        
        self.base1 = QComboBox()
        self.base1.addItems(["2", "8", "10", "16"])
        self.base1.setFixedWidth(60)
        num1_layout.addWidget(QLabel("Base:"))
        num1_layout.addWidget(self.base1)
        layout.addLayout(num1_layout)
        
        # Second number
        num2_layout = QHBoxLayout()
        num2_label = QLabel("Second Number:")
        num2_label.setFixedWidth(100)
        num2_layout.addWidget(num2_label)
        self.add_num2 = QLineEdit()
        self.add_num2.setPlaceholderText("Enter second number")
        num2_layout.addWidget(self.add_num2)
        
        self.base2 = QComboBox()
        self.base2.addItems(["2", "8", "10", "16"])
        self.base2.setFixedWidth(60)
        num2_layout.addWidget(QLabel("Base:"))
        num2_layout.addWidget(self.base2)
        layout.addLayout(num2_layout)
        
        # Add button
        add_btn = QPushButton("Add Numbers")
        add_btn.clicked.connect(self.add_numbers)
        add_btn.setStyleSheet("QPushButton { background-color: #FF9800; } QPushButton:hover { background-color: #f57c00; }")
        layout.addWidget(add_btn)
        
        # Result display
        result_layout = QVBoxLayout()
        result_label = QLabel("Addition Results:")
        result_layout.addWidget(result_label)
        
        self.decimal_result = QTextEdit()
        self.decimal_result.setReadOnly(True)
        self.decimal_result.setPlaceholderText("Decimal result will appear here")
        self.decimal_result.setMaximumHeight(30)
        result_layout.addWidget(QLabel("Decimal:"))
        result_layout.addWidget(self.decimal_result)
        
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
    
    def add_numbers(self):
        try:
            base1 = int(self.base1.currentText())
            base2 = int(self.base2.currentText())
            
            num1 = self.add_num1.text()
            num2 = self.add_num2.text()
            
            decimal, binary, octal, hexadecimal = add_numbers(num1, base1, num2, base2)
            
            self.decimal_result.setPlainText(str(decimal))
            self.binary_result.setPlainText(binary)
            self.octal_result.setPlainText(octal)
            self.hex_result.setPlainText(hexadecimal)
            
            # Adjust height based on content
            self.adjust_text_edit_height(self.decimal_result)
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
            