# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Mon Feb 10 15:12:56 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1373, 909)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_widget_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_widget_layout.setSpacing(0)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_layout.setObjectName("central_widget_layout")
        self.portal = QtWidgets.QFrame(self.centralwidget)
        self.portal.setLineWidth(0)
        self.portal.setObjectName("portal")
        self.portal_buttons_layout = QtWidgets.QVBoxLayout(self.portal)
        self.portal_buttons_layout.setObjectName("portal_buttons_layout")
        self.device_hub = QtWidgets.QToolButton(self.portal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_hub.sizePolicy().hasHeightForWidth())
        self.device_hub.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_window/device_hub"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.device_hub.setIcon(icon)
        self.device_hub.setIconSize(QtCore.QSize(48, 48))
        self.device_hub.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.device_hub.setAutoRaise(True)
        self.device_hub.setObjectName("device_hub")
        self.portal_buttons_layout.addWidget(self.device_hub)
        self.protocol_editor = QtWidgets.QToolButton(self.portal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.protocol_editor.sizePolicy().hasHeightForWidth())
        self.protocol_editor.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main_window/protocol_editor"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.protocol_editor.setIcon(icon1)
        self.protocol_editor.setIconSize(QtCore.QSize(48, 48))
        self.protocol_editor.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.protocol_editor.setAutoRaise(True)
        self.protocol_editor.setObjectName("protocol_editor")
        self.portal_buttons_layout.addWidget(self.protocol_editor)
        self.acquisition = QtWidgets.QToolButton(self.portal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acquisition.sizePolicy().hasHeightForWidth())
        self.acquisition.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/main_window/acquisition"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acquisition.setIcon(icon2)
        self.acquisition.setIconSize(QtCore.QSize(48, 48))
        self.acquisition.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.acquisition.setAutoRaise(True)
        self.acquisition.setObjectName("acquisition")
        self.portal_buttons_layout.addWidget(self.acquisition)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.portal_buttons_layout.addItem(spacerItem)
        self.problems = QtWidgets.QToolButton(self.portal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.problems.sizePolicy().hasHeightForWidth())
        self.problems.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/main_window/problems"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.problems.setIcon(icon3)
        self.problems.setIconSize(QtCore.QSize(48, 48))
        self.problems.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.problems.setAutoRaise(True)
        self.problems.setObjectName("problems")
        self.portal_buttons_layout.addWidget(self.problems)
        self.exit = QtWidgets.QToolButton(self.portal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/main_window/exit"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon4)
        self.exit.setIconSize(QtCore.QSize(48, 48))
        self.exit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.exit.setAutoRaise(True)
        self.exit.setObjectName("exit")
        self.portal_buttons_layout.addWidget(self.exit)
        self.central_widget_layout.addWidget(self.portal)
        self.workspace = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspace.sizePolicy().hasHeightForWidth())
        self.workspace.setSizePolicy(sizePolicy)
        self.workspace.setObjectName("workspace")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.workspace.addWidget(self.page)
        self.central_widget_layout.addWidget(self.workspace)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.device_hub.setText(QtWidgets.QApplication.translate("MainWindow", "Device Hub", None, -1))
        self.protocol_editor.setText(QtWidgets.QApplication.translate("MainWindow", "Protocol\n"
"Editor", None, -1))
        self.acquisition.setText(QtWidgets.QApplication.translate("MainWindow", "Acquisition", None, -1))
        self.problems.setText(QtWidgets.QApplication.translate("MainWindow", "Problems", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))

from . import resources_rc
