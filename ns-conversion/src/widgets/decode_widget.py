from PyQt5.QtWidgets import (QGroupBox, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QComboBox)
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QFontMetrics

from utils.decode import decode_message

class DecodeWidget(QGroupBox):
    def __init__(self):
        super().__init__("Message Decoding")
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 15, 10, 10)
        
        # Key input
        key_layout = QHBoxLayout()
        key_label = QLabel("Secret Key:")
        key_label.setFixedWidth(100)
        key_layout.addWidget(key_label)
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter the same key used for encoding")
        self.key_input.textChanged.connect(self.auto_decode)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        # Input format selection
        format_layout = QHBoxLayout()
        format_label = QLabel("Input Format:")
        format_label.setFixedWidth(100)
        format_layout.addWidget(format_label)
        self.format_combo = QComboBox()
        self.format_combo.addItems(["Decimal", "Hexadecimal"])
        self.format_combo.currentTextChanged.connect(self.auto_decode)
        format_layout.addWidget(self.format_combo)
        layout.addLayout(format_layout)
        
        # Result display - this will expand to fill space
        result_layout = QVBoxLayout()
        result_label = QLabel("Decoded Message:")
        result_layout.addWidget(result_label)
        
        self.decode_result = QTextEdit()
        self.decode_result.setReadOnly(True)
        self.decode_result.setPlaceholderText("Decoded message will appear here when you enter the correct key")
        self.decode_result.setMinimumHeight(80)  # Reasonable minimum height
        
        # Make the text edit expand to fill available space
        result_layout.addWidget(self.decode_result, 1)  # The '1' makes it expand
        
        layout.addLayout(result_layout, 1)  # Make the result section expand too
        
        self.setLayout(layout)
        
        # Store encoded data
        self.encoded_decimal = ""
        self.encoded_hex = ""
        self.encode_key = ""
        
        # Timer for initial adjustment
        self.adjust_timer = QTimer()
        self.adjust_timer.setSingleShot(True)
        self.adjust_timer.timeout.connect(self.adjust_text_edit_height)
        self.adjust_timer.start(100)
    
    def set_encoded_data(self, decimal_values, hex_values, key):
        """Set the encoded data from the encode widget"""
        self.encoded_decimal = decimal_values
        self.encoded_hex = hex_values
        self.encode_key = key
        self.auto_decode()
    
    def auto_decode(self):
        """Automatically decode when key matches"""
        if not self.encoded_decimal or not self.encode_key:
            return
            
        current_key = self.key_input.text()
        
        if current_key == self.encode_key:
            try:
                is_hex = self.format_combo.currentText() == "Hexadecimal"
                encoded_values = self.encoded_hex if is_hex else self.encoded_decimal
                
                result = decode_message(encoded_values, current_key, is_hex)
                self.decode_result.setPlainText(result)
                QTimer.singleShot(50, self.adjust_text_edit_height)
            except ValueError:
                self.decode_result.setPlainText("")
                QTimer.singleShot(50, self.adjust_text_edit_height)
        else:
            self.decode_result.setPlainText("")
            QTimer.singleShot(50, self.adjust_text_edit_height)
    
    def adjust_text_edit_height(self):
        """Adjust the height of the text edit to fit content while allowing expansion"""
        text_edit = self.decode_result
        
        # Get the text content
        text = text_edit.toPlainText()
        if not text:
            text = text_edit.placeholderText()
        
        if not text:
            text_edit.setMinimumHeight(80)
            return
        
        # Calculate ideal height based on content
        available_width = text_edit.viewport().width() - 15
        doc = text_edit.document().clone()
        doc.setTextWidth(available_width)
        ideal_height = doc.size().height() + 25  
        
        # Set minimum height to fit content, but allow expansion
        text_edit.setMinimumHeight(min(int(ideal_height), 300))
    
    def resizeEvent(self, event):
        """Handle resize events to adjust text edit height"""
        super().resizeEvent(event)
        QTimer.singleShot(50, self.adjust_text_edit_height)
    
    def showEvent(self, event):
        """Handle show events to ensure proper sizing"""
        super().showEvent(event)
        QTimer.singleShot(100, self.adjust_text_edit_height)
