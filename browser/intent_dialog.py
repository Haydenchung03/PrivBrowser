from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QSpinBox,
    QComboBox
)


class IntentDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.intent = None
        self.hours = 0
        self.minutes = 0

        self.setWindowTitle("Start Focus Session")
        self.setMinimumWidth(300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("What are you doing?"))

        self.intent_box = QComboBox()
        self.intent_box.addItems([
            "Work",
            "Research",
            "Study",
            "Shopping",
            "Entertainment",
            "Other"
        ])
        layout.addWidget(self.intent_box)

        layout.addWidget(QLabel("How long?"))

        time_layout = QHBoxLayout()

        self.hours_box = QSpinBox()
        self.hours_box.setRange(0, 12)
        self.hours_box.setSuffix(" h")

        self.minutes_box = QSpinBox()
        self.minutes_box.setRange(0, 59)
        self.minutes_box.setSuffix(" m")

        time_layout.addWidget(self.hours_box)
        time_layout.addWidget(self.minutes_box)

        layout.addLayout(time_layout)

        start_btn = QPushButton("Start Session")
        start_btn.clicked.connect(self.accept_session)

        layout.addWidget(start_btn)

        self.setLayout(layout)

    def accept_session(self):

        self.intent = self.intent_box.currentText()
        self.hours = self.hours_box.value()
        self.minutes = self.minutes_box.value()

        self.accept()