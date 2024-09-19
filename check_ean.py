import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

import logging
from log import setup_logger, parse_args

def calculate_ean(ean: str) -> bool:
    """
    Calculate the checksum of an EAN-13 number and verify its validity.

    Args:
        ean (str): The EAN-13 number as a string.

    Returns:
        bool: True if the EAN-13 number is valid, False otherwise.
    """
    if len(ean) != 13 or not ean.isdigit():
        return False

    checksum = 0
    for i, digit in enumerate(ean[:-1]):
        if i % 2 == 0:
            checksum += int(digit)
        else:
            checksum += int(digit) * 3

    check_digit = (10 - (checksum % 10)) % 10
    return check_digit == int(ean[-1])

def config_logger():
    verbose_level_str = parse_args()
    verbose_level = getattr(logging, verbose_level_str.upper(), logging.INFO)
    setup_logger(verbose_level)
    logger = logging.getLogger('ui')
    logger.debug("verbose level was set to %s", verbose_level)
    return logger

class EANChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("checker")
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('EAN-13 Checker')

        self.layout = QVBoxLayout()

        self.ean_input = QLineEdit(self)
        self.ean_input.setPlaceholderText('Enter EAN-13 number')
        self.layout.addWidget(self.ean_input)

        self.check_button = QPushButton('Check EAN-13', self)
        self.check_button.clicked.connect(self.check_ean)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel('', self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def check_ean(self):
        """Check the validity of the entered EAN-13 number and display the result."""
        ean = self.ean_input.text()
        if calculate_ean(ean):
            self.logger.info("%s is a correct EAN-13 number.", ean)
            self.result_label.setText(f"{ean} is a correct EAN-13 number.")
        else:
            self.logger.error("%s is not a correct EAN-13 number.", ean)
            self.result_label.setText(f"{ean} is not a correct EAN-13 number.")
            return


if __name__ == '__main__':
    # config logger
    logger = config_logger()
    logger.info("building ui...")
    app = QApplication(sys.argv)
    ex = EANChecker()
    logger.info("app was build and will be shown straight ahead on the screen.")
    ex.show()
    sys.exit(app.exec())
