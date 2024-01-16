from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QGuiApplication, QPixmap

class Blackout(QWidget):
    def __init__(self, parent=None, image_path=None):
        super().__init__(parent)
        self.setWindowTitle("Blackout")
        self.setWindowModality(Qt.WindowModal)  # Make the window modal (covers everything)
        self.setStyleSheet("background-color: black;")
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove window borders

        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        print(screen_geometry)
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

    def start_blackout(self, duration):
        self.show()
        self.timer.start(duration * 1000)  # Convert seconds to milliseconds

if __name__ == "__main__":
    app = QApplication([])
    
    # blackout = Blackout()
    # blackout.start_blackout(5)  # Set blackout duration in seconds
    
    image_path="./img1.jpg"
    blackout = Blackout(parent=None, image_path=image_path)
    blackout.start_blackout(10)
    
    app.exec_()
