# Application styles
APP_STYLES = """
    QMainWindow {
        background-color: #2b2b2b;
    }
    QLabel {
        color: #ffffff;
        font-size: 14px;
    }
    QPushButton {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        margin: 4px 2px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #3d8b40;
    }
    QGroupBox {
        font-weight: bold;
        border: 2px solid #4CAF50;
        border-radius: 8px;
        margin-top: 1ex;
        padding-top: 10px;
        background-color: #3c3c3c;
        color: #ffffff;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px 0 5px;
        color: #4CAF50;
    }
    QLineEdit, QTextEdit, QComboBox {
        background-color: #ffffff;
        border: 1px solid #cccccc;
        border-radius: 4px;
        padding: 5px;
        font-size: 14px;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left-width: 1px;
        border-left-color: darkgray;
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;
    }
    QTextEdit {
        font-family: 'Courier New';
        min-height: 30px;
        max-height: 200px; /* Maximum height to prevent excessive growth */
    }
    QMessageBox {
        background-color: #2b2b2b;
    }
    QMessageBox QLabel {
        color: #ffffff;
        font-size: 14px;
    }
    QMessageBox QPushButton {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        margin: 4px 2px;
        border-radius: 4px;
    }
    QMessageBox QPushButton:hover {
        background-color: #45a049;
    }
"""