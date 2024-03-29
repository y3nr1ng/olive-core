from functools import partial
import logging
import os

from olive.ui.mainwindow import MainWindowView as _MainWindowView
from olive.ui.mainwindow import Portal

from ..base import QMainWindowViewBase

__all__ = ["MainWindowView"]

logger = logging.getLogger(__name__)


class MainWindowView(_MainWindowView, QMainWindowViewBase):
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "view.ui")
        super().__init__(path)

    ##

    def set_change_workspace_action(self, action):
        self.device_hub.clicked.connect(partial(action, Portal.DeviceHub))
        self.protocol_editor.clicked.connect(partial(action, Portal.ProtocolEditor))
        self.acquisition.clicked.connect(partial(action, Portal.Acquisition))

    def set_exit_action(self, action):
        self.exit.clicked.connect(action)

    def add_workspace(self, view):
        index = self.workspace.addWidget(view)
        return index

    ##

    def change_workspace(self, index):
        self.workspace.setCurrentIndex(index)

