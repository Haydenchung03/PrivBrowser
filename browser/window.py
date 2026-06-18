from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QMessageBox
)

from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView

from .intent_dialog import IntentDialog
from .activity_bar import ActivityBar
from .session_manager import SessionManager


class BrowserWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.session = SessionManager()
        self.session.session_ended.connect(self.on_session_end)

        self.start_session()

        self.setWindowTitle("Privacy Browser")
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com"))

        self.activity_bar = ActivityBar(self.session)

        container = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.activity_bar)
        layout.addWidget(self.browser)

        container.setLayout(layout)
        self.setCentralWidget(container)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        back_btn = QAction("←", self)
        back_btn.triggered.connect(self.browser.back)
        toolbar.addAction(back_btn)

        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_btn)

        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(
            lambda: self.browser.setUrl(QUrl("https://duckduckgo.com"))
        )
        toolbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        toolbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    # -------------------------
    # Session handling
    # -------------------------

    def start_session(self):

        dialog = IntentDialog()

        if dialog.exec():

            self.session.start_session(
                dialog.intent,
                dialog.hours,
                dialog.minutes
            )
        else:
            self.session.start_session("Other", 0, 30)

    def on_session_end(self):

        msg = QMessageBox(self)
        msg.setWindowTitle("Session Complete")

        msg.setText(
            f"Time's up for: {self.session.intent}"
        )

        new_task_btn = msg.addButton(
            "New Task",
            QMessageBox.ButtonRole.AcceptRole
        )

        end_btn = msg.addButton(
            "End Session",
            QMessageBox.ButtonRole.RejectRole
        )

        msg.exec()

        if msg.clickedButton() == end_btn:
            self.close()

        else:
            self.session.reset()
            self.start_session()

    # -------------------------
    # Browser
    # -------------------------

    def navigate(self):

        url = self.url_bar.text().strip()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())