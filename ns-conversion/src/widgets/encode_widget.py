from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox)
from PyQt5.QtCore import pyqtSignal

from utils.encode import encode_message

class EncodeWidget(QGroupBox):
    encoded = pyqtSignal(str, str, str)  # signal: decimal_values, hex_values, key
    
    def __init__(self):
        super().__init__("Message Encoding")
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Message input
        message_layout = QHBoxLayout()
        message_label = QLabel("Message:")
        message_label.setFixedWidth(100)
        message_layout.addWidget(message_label)
        self.encode_input = QLineEdit()
        self.encode_input.setPlaceholderText("Enter message to encode")
        message_layout.addWidget(self.encode_input)
        layout.addLayout(message_layout)
        
        # Key input
        key_layout = QHBoxLayout()
        key_label = QLabel("Secret Key:")
        key_label.setFixedWidth(100)
        key_layout.addWidget(key_label)
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter decimal key")
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        # Encode button
        encode_btn = QPushButton("Encode Message")
        encode_btn.clicked.connect(self.encode_text)
        encode_btn.setStyleSheet("QPushButton { background-color: #9C27B0; } QPushButton:hover { background-color: #7b1fa2; }")
        layout.addWidget(encode_btn)
        
        # Result display
        result_layout = QVBoxLayout()
        result_label = QLabel("Encoded Results:")
        result_layout.addWidget(result_label)
        
        self.decimal_result = QTextEdit()
        self.decimal_result.setReadOnly(True)
        self.decimal_result.setPlaceholderText("Decimal encoded values will appear here")
        self.decimal_result.setMaximumHeight(30)
        result_layout.addWidget(QLabel("Decimal Values:"))
        result_layout.addWidget(self.decimal_result)
        
        self.hex_result = QTextEdit()
        self.hex_result.setReadOnly(True)
        self.hex_result.setPlaceholderText("Hexadecimal encoded values will appear here")
        self.hex_result.setMaximumHeight(30)
        result_layout.addWidget(QLabel("Hexadecimal Values:"))
        result_layout.addWidget(self.hex_result)
        
        layout.addLayout(result_layout)
        
        self.setLayout(layout)
        
        # Store the latest encoded data
        self.latest_decimal_values = ""
        self.latest_hex_values = ""
        self.latest_key = ""
    
    def encode_text(self):
        try:
            message = self.encode_input.text()
            key = self.key_input.text()
            
            decimal_values, hex_values = encode_message(message, key)
            
            self.decimal_result.setPlainText(", ".join(decimal_values))
            self.hex_result.setPlainText(", ".join(hex_values))
            
            # Store the encoded data
            self.latest_decimal_values = ", ".join(decimal_values)
            self.latest_hex_values = ", ".join(hex_values)
            self.latest_key = key
            
            # Emit signal with encoded data
            self.encoded.emit(self.latest_decimal_values, self.latest_hex_values, self.latest_key)
            
            # Adjust height based on content
            self.adjust_text_edit_height(self.decimal_result)
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
            