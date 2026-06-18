from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer


class ActivityBar(QWidget):

    def __init__(self, session_manager):
        super().__init__()

        self.session = session_manager

        layout = QHBoxLayout()
        layout.setContentsMargins(4, 1, 4, 1)
        layout.setSpacing(8)

        self.setLayout(layout)
        self.setFixedHeight(18)

        self.intent_label = QLabel()
        self.time_label = QLabel()

        style = "color: #777; font-size: 10px;"

        self.intent_label.setStyleSheet(style)
        self.time_label.setStyleSheet(style)

        layout.addWidget(self.intent_label)
        layout.addStretch()
        layout.addWidget(self.time_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def format_time(self, seconds):

        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60

        return f"{h:02d}:{m:02d}:{s:02d}"

    def update(self):

        self.session.tick()

        self.intent_label.setText(
            f"{self.session.intent}"
        )

        self.time_label.setText(
            self.format_time(self.session.remaining_seconds)
        )