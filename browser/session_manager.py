from PyQt6.QtCore import QObject, pyqtSignal


class SessionManager(QObject):

    session_ended = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.intent = "Other"
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.active = False

    def start_session(self, intent, hours, minutes):

        self.intent = intent
        self.total_seconds = (hours * 3600) + (minutes * 60)
        self.remaining_seconds = self.total_seconds
        self.active = True

    def tick(self):

        if not self.active:
            return

        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1

        if self.remaining_seconds <= 0:
            self.active = False
            self.session_ended.emit()

    def reset(self):
        self.intent = "Other"
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.active = False