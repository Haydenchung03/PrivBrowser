from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QLineEdit
)

from PyQt6.QtGui import QAction

from PyQt6.QtWebEngineWidgets import QWebEngineView

from .settings import create_private_profile


class BrowserWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Privacy Browser")

        self.resize(1200, 800)

        profile = create_private_profile()

        self.browser = QWebEngineView()

        self.browser.setUrl(
            QUrl("https://duckduckgo.com")
        )

        self.setCentralWidget(self.browser)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        back_btn = QAction("←", self)
        back_btn.triggered.connect(
            self.browser.back
        )
        toolbar.addAction(back_btn)

        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(
            self.browser.forward
        )
        toolbar.addAction(forward_btn)

        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(
            self.browser.reload
        )
        toolbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(
            self.go_home
        )
        toolbar.addAction(home_btn)

        self.url_bar = QLineEdit()

        self.url_bar.returnPressed.connect(
            self.navigate
        )

        toolbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(
            self.update_url
        )

    def go_home(self):
        self.browser.setUrl(
            QUrl("https://duckduckgo.com")
        )

    def navigate(self):
        url = self.url_bar.text().strip()

        if not url.startswith(
            ("http://", "https://")
        ):
            url = "https://" + url

        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())