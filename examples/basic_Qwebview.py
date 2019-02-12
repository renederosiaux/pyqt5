#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python3 v3.5 PyQt5 v5.9

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

if __name__ == '__main__':
    app = QApplication(sys.argv)

    page = QWebEnginePage()
    page.setUrl(QUrl("https://www.google.fr/"))
    print ("page")

    view = QWebEngineView()
    view.setPage(page)

    view.resize(1024, 600)
    view.show()

    sys.exit(app.exec_())
