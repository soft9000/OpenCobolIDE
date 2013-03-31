# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ide.ui'
#
# Created: Sun Mar 31 18:51:12 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 738)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.page_2)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarFile = QtGui.QToolBar(MainWindow)
        self.toolBarFile.setObjectName("toolBarFile")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFile)
        self.toolBarCode = QtGui.QToolBar(MainWindow)
        self.toolBarCode.setObjectName("toolBarCode")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCode)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidgetLogs = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidgetLogs.setObjectName("tabWidgetLogs")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidgetErrors = QtGui.QListWidget(self.tab_3)
        self.listWidgetErrors.setObjectName("listWidgetErrors")
        self.gridLayout_4.addWidget(self.listWidgetErrors, 0, 0, 1, 1)
        self.tabWidgetLogs.addTab(self.tab_3, icon, "")
        self.tabProgramOutput = QtGui.QWidget()
        self.tabProgramOutput.setObjectName("tabProgramOutput")
        self.gridLayout_5 = QtGui.QGridLayout(self.tabProgramOutput)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plainTextEditOutput = QtGui.QPlainTextEdit(self.tabProgramOutput)
        self.plainTextEditOutput.setObjectName("plainTextEditOutput")
        self.gridLayout_5.addWidget(self.plainTextEditOutput, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ide-icons/rc/utilities-terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidgetLogs.addTab(self.tabProgramOutput, icon1, "")
        self.gridLayout_3.addWidget(self.tabWidgetLogs, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 765, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuCobol = QtGui.QMenu(self.menuBar)
        self.menuCobol.setObjectName("menuCobol")
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ide-icons/rc/system-log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCompile = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ide-icons/rc/applications-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompile.setIcon(icon3)
        self.actionCompile.setIconVisibleInMenu(True)
        self.actionCompile.setObjectName("actionCompile")
        self.actionRun = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ide-icons/rc/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon4)
        self.actionRun.setIconVisibleInMenu(True)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ide-icons/rc/dialog-information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon7)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/ide-icons/rc/view-fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullscreen.setIcon(icon8)
        self.actionFullscreen.setIconVisibleInMenu(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionProgram = QtGui.QAction(MainWindow)
        self.actionProgram.setCheckable(True)
        self.actionProgram.setChecked(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/ide-icons/rc/application-x-executable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProgram.setIcon(icon9)
        self.actionProgram.setIconVisibleInMenu(True)
        self.actionProgram.setObjectName("actionProgram")
        self.actionSubprogram = QtGui.QAction(MainWindow)
        self.actionSubprogram.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/ide-icons/rc/application-x-sharedlib.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSubprogram.setIcon(icon10)
        self.actionSubprogram.setIconVisibleInMenu(True)
        self.actionSubprogram.setObjectName("actionSubprogram")
        self.actionNew = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon11)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/ide-icons/rc/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon12)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.toolBarFile.addAction(self.actionNew)
        self.toolBarFile.addAction(self.actionOpen)
        self.toolBarFile.addSeparator()
        self.toolBarFile.addAction(self.actionSave)
        self.toolBarCode.addAction(self.actionProgram)
        self.toolBarCode.addAction(self.actionSubprogram)
        self.toolBarCode.addSeparator()
        self.toolBarCode.addAction(self.actionCompile)
        self.toolBarCode.addAction(self.actionRun)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionFullscreen)
        self.menuCobol.addAction(self.actionProgram)
        self.menuCobol.addAction(self.actionSubprogram)
        self.menuCobol.addSeparator()
        self.menuCobol.addAction(self.actionCompile)
        self.menuCobol.addAction(self.actionRun)
        self.menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuCobol.menuAction())
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)
        self.tabWidgetLogs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenCobol IDE", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBarFile.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Tollbar File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBarCode.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Toolbar Code", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Logs window", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Compiler", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLogs.setTabToolTip(self.tabWidgetLogs.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Show compiler log", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetLogs.setTabText(self.tabWidgetLogs.indexOf(self.tabProgramOutput), QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCobol.setTitle(QtGui.QApplication.translate("MainWindow", "Cobol", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit application (Ctrl+Q)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompile.setText(QtGui.QApplication.translate("MainWindow", "Compile", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompile.setToolTip(QtGui.QApplication.translate("MainWindow", "Compile the current file (F8)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompile.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setToolTip(QtGui.QApplication.translate("MainWindow", "Run the current file (F5)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setToolTip(QtGui.QApplication.translate("MainWindow", "About OpenCobol IDE (F1)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("MainWindow", "Save current file (Ctrl+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setToolTip(QtGui.QApplication.translate("MainWindow", "Save current file as (Ctrl+Shift+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setText(QtGui.QApplication.translate("MainWindow", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setToolTip(QtGui.QApplication.translate("MainWindow", "Toggle fullscreen (F12)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setShortcut(QtGui.QApplication.translate("MainWindow", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProgram.setText(QtGui.QApplication.translate("MainWindow", "Program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProgram.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Tells the ide to compile the current file as an executable (.exe)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSubprogram.setText(QtGui.QApplication.translate("MainWindow", "Subprogram", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSubprogram.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Tells the ide to compile the current file as a subprogram (.so)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("MainWindow", "New file (Ctrl+N)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setToolTip(QtGui.QApplication.translate("MainWindow", "Open a file (Ctrl+O)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))

import ide_rc
