import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QGuiApplication, QPixmap, QFont

class Blackout(QWidget):
    def __init__(self, parent=None, image_path=None, text="", text_position="center"):
        super().__init__(parent)
        self.setWindowTitle("Blackout")

        # Make the window modal (covers everything)
        self.setWindowModality(Qt.WindowModal)

        # Remove window borders
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Resize to match screen dimensions
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(screen_geometry)

        # Timer to control duration and window closing
        self.timer = QTimer()
        self.timer.timeout.connect(self.close)

        if image_path:
            # Load and scale image to fit the window
            self.image = QPixmap(image_path).scaled(self.size(), Qt.KeepAspectRatio)
        else:
            # Set background color to black if no image provided
            self.setStyleSheet("background-color: black;")

        # Create text label
        self.text_label = QLabel(self)
        self.text_label.setText(text)
        self.text_label.setFont(QFont("Arial", 20))  # Adjust font as needed
        self.text_label.setStyleSheet(f"color: gray;")  # Set text color
        self.set_text_position(text_position)

    def set_text_position(self, position):
        if position == "center":
            self.text_label.setAlignment(Qt.AlignCenter)
        elif position == "top":
            self.text_label.setAlignment(Qt.AlignTop)
        elif position == "bottom":
            self.text_label.setAlignment(Qt.AlignBottom)
        elif position == "left":
            self.text_label.setAlignment(Qt.AlignLeft)
        elif position == "right":
            self.text_label.setAlignment(Qt.AlignRight)
        else:
            print("Invalid text position specified. Using center alignment.")
            self.text_label.setAlignment(Qt.AlignCenter)

    def start_blackout(self, duration):
        self.show()
        self.timer.start(duration * 1000)  # Convert seconds to milliseconds

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a blackout with text
    blackout = Blackout(text="This is a blackout message!", text_position="top")
    blackout.start_blackout(5)

    sys.exit(app.exec_())
