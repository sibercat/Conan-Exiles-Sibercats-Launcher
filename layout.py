# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 495)
        MainWindow.setMinimumSize(QtCore.QSize(942, 495))
        MainWindow.setMaximumSize(QtCore.QSize(942, 495))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 942, 495))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.tab_8)
        self.groupBox_7.setGeometry(QtCore.QRect(790, 170, 141, 201))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEditExternaliP = QtWidgets.QLineEdit(parent=self.groupBox_7)
        self.lineEditExternaliP.setEnabled(True)
        self.lineEditExternaliP.setGeometry(QtCore.QRect(15, 85, 113, 20))
        self.lineEditExternaliP.setObjectName("lineEditExternaliP")
        self.labelExternaliP = QtWidgets.QLabel(parent=self.groupBox_7)
        self.labelExternaliP.setGeometry(QtCore.QRect(15, 65, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelExternaliP.setFont(font)
        self.labelExternaliP.setObjectName("labelExternaliP")
        self.labelLocalIp = QtWidgets.QLabel(parent=self.groupBox_7)
        self.labelLocalIp.setGeometry(QtCore.QRect(15, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLocalIp.setFont(font)
        self.labelLocalIp.setObjectName("labelLocalIp")
        self.lineEditIPv4addressLocal = QtWidgets.QLineEdit(parent=self.groupBox_7)
        self.lineEditIPv4addressLocal.setEnabled(True)
        self.lineEditIPv4addressLocal.setGeometry(QtCore.QRect(15, 40, 113, 20))
        self.lineEditIPv4addressLocal.setObjectName("lineEditIPv4addressLocal")
        self.line_3 = QtWidgets.QFrame(parent=self.groupBox_7)
        self.line_3.setGeometry(QtCore.QRect(0, 100, 141, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.labelportProtocalbeingUsed = QtWidgets.QLabel(parent=self.groupBox_7)
        self.labelportProtocalbeingUsed.setGeometry(QtCore.QRect(11, 120, 131, 20))
        self.labelportProtocalbeingUsed.setObjectName("labelportProtocalbeingUsed")
        self.linePortProtocalbeingUsed = QtWidgets.QLineEdit(parent=self.groupBox_7)
        self.linePortProtocalbeingUsed.setEnabled(True)
        self.linePortProtocalbeingUsed.setGeometry(QtCore.QRect(15, 140, 113, 20))
        self.linePortProtocalbeingUsed.setText("")
        self.linePortProtocalbeingUsed.setFrame(True)
        self.linePortProtocalbeingUsed.setObjectName("linePortProtocalbeingUsed")
        self.pushButton18 = QtWidgets.QPushButton(parent=self.groupBox_7)
        self.pushButton18.setGeometry(QtCore.QRect(30, 170, 75, 23))
        self.pushButton18.setObjectName("pushButton18")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tab_8)
        self.groupBox_5.setGeometry(QtCore.QRect(770, 10, 161, 141))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton13 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButton13.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.pushButton13.setToolTipDuration(-1)
        self.pushButton13.setObjectName("pushButton13")
        self.pushButton14 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButton14.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.pushButton14.setObjectName("pushButton14")
        self.pushButton16 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButton16.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.pushButton16.setObjectName("pushButton16")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab_8)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 611, 65))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton1 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton1.setGeometry(QtCore.QRect(10, 20, 201, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton3 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton3.setGeometry(QtCore.QRect(220, 20, 121, 31))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton4.setGeometry(QtCore.QRect(480, 20, 121, 31))
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton5 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton5.setGeometry(QtCore.QRect(350, 20, 121, 31))
        self.pushButton5.setObjectName("pushButton5")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab_8)
        self.groupBox.setGeometry(QtCore.QRect(1, 90, 431, 65))
        self.groupBox.setObjectName("groupBox")
        self.pushButton2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton2.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton10 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton10.setGeometry(QtCore.QRect(140, 20, 121, 31))
        self.pushButton10.setObjectName("pushButton10")
        self.pushButton12 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton12.setGeometry(QtCore.QRect(270, 20, 121, 31))
        self.pushButton12.setObjectName("pushButton12")
        self.progressBar = QtWidgets.QProgressBar(parent=self.groupBox)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(270, 50, 156, 15))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_8)
        self.groupBox_2.setGeometry(QtCore.QRect(1, 170, 781, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.groupBox_2)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 331, 81))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton7 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton7.setGeometry(QtCore.QRect(100, 10, 121, 31))
        self.pushButton7.setObjectName("pushButton7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton8 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton8.setGeometry(QtCore.QRect(100, 10, 121, 31))
        self.pushButton8.setObjectName("pushButton8")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton9 = QtWidgets.QPushButton(parent=self.tab_4)
        self.pushButton9.setGeometry(QtCore.QRect(100, 10, 121, 31))
        self.pushButton9.setObjectName("pushButton9")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton11 = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton11.setGeometry(QtCore.QRect(100, 10, 141, 31))
        self.pushButton11.setObjectName("pushButton11")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton15 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton15.setGeometry(QtCore.QRect(100, 10, 151, 31))
        self.pushButton15.setObjectName("pushButton15")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton17 = QtWidgets.QPushButton(parent=self.tab_6)
        self.pushButton17.setGeometry(QtCore.QRect(80, 10, 201, 31))
        self.pushButton17.setObjectName("pushButton17")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton19 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton19.setGeometry(QtCore.QRect(100, 10, 171, 31))
        self.pushButton19.setObjectName("pushButton19")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 0, 431, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBoxGlorb_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxGlorb_R.setGeometry(QtCore.QRect(50, 40, 51, 20))
        self.checkBoxGlorb_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxGlorb_R.setObjectName("checkBoxGlorb_R")
        self.checkBoxWallpaper_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxWallpaper_R.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.checkBoxWallpaper_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxWallpaper_R.setObjectName("checkBoxWallpaper_R")
        self.pushButton20 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.pushButton20.setGeometry(QtCore.QRect(190, 170, 75, 23))
        self.pushButton20.setObjectName("pushButton20")
        self.line_2 = QtWidgets.QFrame(parent=self.groupBox_6)
        self.line_2.setGeometry(QtCore.QRect(0, 150, 431, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBoxNPCSpawn_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxNPCSpawn_R.setGeometry(QtCore.QRect(10, 60, 91, 20))
        self.checkBoxNPCSpawn_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxNPCSpawn_R.setObjectName("checkBoxNPCSpawn_R")
        self.checkBoxLootSpawner_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxLootSpawner_R.setGeometry(QtCore.QRect(10, 80, 91, 20))
        self.checkBoxLootSpawner_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxLootSpawner_R.setObjectName("checkBoxLootSpawner_R")
        self.checkBoxPortal_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxPortal_R.setGeometry(QtCore.QRect(50, 100, 51, 20))
        self.checkBoxPortal_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxPortal_R.setObjectName("checkBoxPortal_R")
        self.checkBoxFlaggi_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxFlaggi_R.setGeometry(QtCore.QRect(50, 120, 51, 20))
        self.checkBoxFlaggi_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxFlaggi_R.setObjectName("checkBoxFlaggi_R")
        self.checkBoxThespian_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxThespian_R.setGeometry(QtCore.QRect(30, 140, 71, 20))
        self.checkBoxThespian_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxThespian_R.setObjectName("checkBoxThespian_R")
        self.checkBoxEgress_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxEgress_R.setGeometry(QtCore.QRect(130, 20, 61, 20))
        self.checkBoxEgress_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxEgress_R.setObjectName("checkBoxEgress_R")
        self.checkBoxCamLoc_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxCamLoc_R.setGeometry(QtCore.QRect(120, 40, 71, 20))
        self.checkBoxCamLoc_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxCamLoc_R.setObjectName("checkBoxCamLoc_R")
        self.checkBoxPippijack_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxPippijack_R.setGeometry(QtCore.QRect(120, 60, 71, 20))
        self.checkBoxPippijack_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxPippijack_R.setObjectName("checkBoxPippijack_R")
        self.checkBoxTZone_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTZone_R.setGeometry(QtCore.QRect(140, 80, 51, 20))
        self.checkBoxTZone_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTZone_R.setObjectName("checkBoxTZone_R")
        self.checkBoxTTime_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTTime_R.setGeometry(QtCore.QRect(140, 100, 51, 20))
        self.checkBoxTTime_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTTime_R.setObjectName("checkBoxTTime_R")
        self.checkBoxTControl_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTControl_R.setGeometry(QtCore.QRect(120, 120, 71, 20))
        self.checkBoxTControl_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTControl_R.setObjectName("checkBoxTControl_R")
        self.checkBoxTPlatform_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTPlatform_R.setGeometry(QtCore.QRect(120, 140, 71, 20))
        self.checkBoxTPlatform_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTPlatform_R.setObjectName("checkBoxTPlatform_R")
        self.checkBoxTSeq_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTSeq_R.setGeometry(QtCore.QRect(240, 20, 51, 20))
        self.checkBoxTSeq_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTSeq_R.setObjectName("checkBoxTSeq_R")
        self.checkBoxTRand_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTRand_R.setGeometry(QtCore.QRect(230, 40, 61, 20))
        self.checkBoxTRand_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTRand_R.setObjectName("checkBoxTRand_R")
        self.checkBoxTPlate_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTPlate_R.setGeometry(QtCore.QRect(230, 60, 61, 20))
        self.checkBoxTPlate_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTPlate_R.setObjectName("checkBoxTPlate_R")
        self.checkBoxTCombiner_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxTCombiner_R.setGeometry(QtCore.QRect(210, 80, 81, 20))
        self.checkBoxTCombiner_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxTCombiner_R.setObjectName("checkBoxTCombiner_R")
        self.checkBoxMarker_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxMarker_R.setGeometry(QtCore.QRect(230, 100, 61, 20))
        self.checkBoxMarker_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxMarker_R.setObjectName("checkBoxMarker_R")
        self.checkBoxRePlaceable_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxRePlaceable_R.setGeometry(QtCore.QRect(210, 120, 81, 20))
        self.checkBoxRePlaceable_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxRePlaceable_R.setObjectName("checkBoxRePlaceable_R")
        self.checkBoxPippiNote_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxPippiNote_R.setGeometry(QtCore.QRect(210, 140, 81, 20))
        self.checkBoxPippiNote_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxPippiNote_R.setObjectName("checkBoxPippiNote_R")
        self.checkBoxNPCSummoner_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxNPCSummoner_R.setGeometry(QtCore.QRect(310, 20, 101, 20))
        self.checkBoxNPCSummoner_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxNPCSummoner_R.setObjectName("checkBoxNPCSummoner_R")
        self.checkBoxEasel_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxEasel_R.setGeometry(QtCore.QRect(360, 40, 51, 20))
        self.checkBoxEasel_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxEasel_R.setObjectName("checkBoxEasel_R")
        self.checkBoxMusiqBox_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxMusiqBox_R.setGeometry(QtCore.QRect(340, 60, 71, 20))
        self.checkBoxMusiqBox_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxMusiqBox_R.setObjectName("checkBoxMusiqBox_R")
        self.checkBoxLazor_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxLazor_R.setGeometry(QtCore.QRect(340, 80, 71, 20))
        self.checkBoxLazor_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxLazor_R.setObjectName("checkBoxLazor_R")
        self.checkBoxCryptex_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxCryptex_R.setGeometry(QtCore.QRect(340, 100, 71, 20))
        self.checkBoxCryptex_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxCryptex_R.setObjectName("checkBoxCryptex_R")
        self.checkBoxCheckpoint_R = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.checkBoxCheckpoint_R.setGeometry(QtCore.QRect(330, 120, 81, 20))
        self.checkBoxCheckpoint_R.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBoxCheckpoint_R.setObjectName("checkBoxCheckpoint_R")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget_2.addTab(self.tab_9, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sibercats Launcher v0.0.49"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Network"))
        self.labelExternaliP.setText(_translate("MainWindow", "External IP:"))
        self.labelLocalIp.setText(_translate("MainWindow", "Ipv4 Address Local:"))
        self.labelportProtocalbeingUsed.setText(_translate("MainWindow", "Check Port Being Used:"))
        self.linePortProtocalbeingUsed.setToolTip(_translate("MainWindow", "<html><head/><body><p>Check if the given port on UDP and TCP protocols is being used on Local IPv4 Address</p><p>Can scan multiple ports at once by using commas to separate 000,000,000</p></body></html>"))
        self.linePortProtocalbeingUsed.setPlaceholderText(_translate("MainWindow", "         UDP/TCP Port"))
        self.pushButton18.setText(_translate("MainWindow", "Check Port"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Other Tools:"))
        self.pushButton13.setToolTip(_translate("MainWindow", "<html><head/><body><p>ItemTable<span style=\" font-weight:600;\"> ID Stripper {.txt Column} </span>will extract IDs from a .txt file from column of numbers</p><p>1</p><p>2</p><p>3</p></body></html>"))
        self.pushButton13.setText(_translate("MainWindow", "ID Stripper {.txt Column}"))
        self.pushButton14.setToolTip(_translate("MainWindow", "<html><head/><body><p>ItemTable <span style=\" font-weight:600;\">ID stripper </span>{.json} ItemTable has to be in .json format.</p></body></html>"))
        self.pushButton14.setText(_translate("MainWindow", "ID Stripper {.json}"))
        self.pushButton16.setToolTip(_translate("MainWindow", "<html><head/><body><p>ItemTable <span style=\" font-weight:600;\">ID stripper </span>{csv} ItemTable has to be in .csv format.</p></body></html>"))
        self.pushButton16.setText(_translate("MainWindow", "ID Stripper {.csv}"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Main:"))
        self.pushButton1.setToolTip(_translate("MainWindow", "<html><head/><body><p>This will open DedicatedServerLauncher1706.exe</p></body></html>"))
        self.pushButton1.setText(_translate("MainWindow", "Start Conan Exiles Server Launcher"))
        self.pushButton3.setToolTip(_translate("MainWindow", "<html><head/><body><p>This will open modlist.txt</p><p>DedicatedServerLauncher\\ConanExilesDedicatedServer\\ConanSandbox\\Mods\\modlist.txt</p></body></html>"))
        self.pushButton3.setText(_translate("MainWindow", "Open modlist.txt"))
        self.pushButton4.setToolTip(_translate("MainWindow", "<html><head/><body><p>This will delete all files inside: DedicatedServerLauncher\\ConanExilesDedicatedServer\\ConanSandbox\\Saved\\Logs</p></body></html>"))
        self.pushButton4.setText(_translate("MainWindow", "Delete Saved Logs"))
        self.pushButton5.setToolTip(_translate("MainWindow", "<html><head/><body><p>This will open ConanSandbox.log</p><p>DedicatedServerLauncher\\ConanExilesDedicatedServer\\ConanSandbox\\Saved\\Logs\\ConanSandbox.log</p></body></html>"))
        self.pushButton5.setText(_translate("MainWindow", "Open .log"))
        self.groupBox.setTitle(_translate("MainWindow", "SQL Database:"))
        self.pushButton2.setToolTip(_translate("MainWindow", "<html><head/><body><p>This will check integrity of your game.db</p><p>DedicatedServerLauncher\\ConanExilesDedicatedServer\\ConanSandbox\\Saved\\game.db</p></body></html>"))
        self.pushButton2.setText(_translate("MainWindow", "Check DB Integrity"))
        self.pushButton10.setText(_translate("MainWindow", "Optimize/Vacuum"))
        self.pushButton12.setText(_translate("MainWindow", "Try To Repair DB"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DB Clean Up:"))
        self.pushButton7.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to remove every trace of <span style=\" font-weight:600;\">ExilesExtreme Mod </span>from game.db</p></body></html>"))
        self.pushButton7.setText(_translate("MainWindow", "Remove All [EE]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "[EE]"))
        self.pushButton8.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to remove every trace of <span style=\" font-weight:600;\">The age of calamitous Mod </span>from game.db</p></body></html>"))
        self.pushButton8.setText(_translate("MainWindow", "Remove All [AOC]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "[AOC]"))
        self.pushButton9.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to remove every trace of <span style=\" font-weight:600;\">Endgame Extended Weapon Arsenal Mod </span>from game.db</p></body></html>"))
        self.pushButton9.setText(_translate("MainWindow", "Remove All [EEWA]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "[EEWA]"))
        self.pushButton11.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to remove every trace of <span style=\" font-weight:600;\">Emberlight </span>from game.db</p></body></html>"))
        self.pushButton11.setText(_translate("MainWindow", "Remove All [Emberlight]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "[Emberlight]"))
        self.pushButton15.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to Clean Up <span style=\" font-weight:600;\">Savage Wilds </span>from savagewilds_game.db. Because this is a map mod we can only delete what has been made by players.</p></body></html>"))
        self.pushButton15.setText(_translate("MainWindow", "Clean Up [Savage Wilds]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "[Savage Wilds]"))
        self.pushButton17.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to Clean Up <span style=\" font-weight:600;\">Savage Wilds </span>from savagewilds_game.db. Because this is a map mod we can only delete what has been made by players.</p></body></html>"))
        self.pushButton17.setText(_translate("MainWindow", "Remove All [Shimas Compendium]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "[Shimas Compendium]"))
        self.pushButton19.setToolTip(_translate("MainWindow", "<html><head/><body><p>This is going to remove every trace of <span style=\" font-weight:600;\">ExilesExtreme Mod </span>from game.db</p></body></html>"))
        self.pushButton19.setText(_translate("MainWindow", "Remove All [Warrior Mutator]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "[Warrior Mutator]"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Remove Pippi:"))
        self.checkBoxGlorb_R.setText(_translate("MainWindow", "Glorb"))
        self.checkBoxWallpaper_R.setText(_translate("MainWindow", "Wallpaper"))
        self.pushButton20.setText(_translate("MainWindow", "Select DB"))
        self.checkBoxNPCSpawn_R.setText(_translate("MainWindow", "NPCSpawner"))
        self.checkBoxLootSpawner_R.setText(_translate("MainWindow", "LootSpawner"))
        self.checkBoxPortal_R.setText(_translate("MainWindow", "Portal"))
        self.checkBoxFlaggi_R.setText(_translate("MainWindow", "Flaggi"))
        self.checkBoxThespian_R.setText(_translate("MainWindow", "Thespian"))
        self.checkBoxEgress_R.setText(_translate("MainWindow", "Egress"))
        self.checkBoxCamLoc_R.setText(_translate("MainWindow", "CamLoc"))
        self.checkBoxPippijack_R.setText(_translate("MainWindow", "Pippijack"))
        self.checkBoxTZone_R.setText(_translate("MainWindow", "TZone"))
        self.checkBoxTTime_R.setText(_translate("MainWindow", "TTime"))
        self.checkBoxTControl_R.setText(_translate("MainWindow", "TControl"))
        self.checkBoxTPlatform_R.setText(_translate("MainWindow", "TPlatform"))
        self.checkBoxTSeq_R.setText(_translate("MainWindow", "TSeq"))
        self.checkBoxTRand_R.setText(_translate("MainWindow", "TRand"))
        self.checkBoxTPlate_R.setText(_translate("MainWindow", "TPlate"))
        self.checkBoxTCombiner_R.setText(_translate("MainWindow", "TCombiner"))
        self.checkBoxMarker_R.setText(_translate("MainWindow", "Marker"))
        self.checkBoxRePlaceable_R.setText(_translate("MainWindow", "RePlaceable"))
        self.checkBoxPippiNote_R.setText(_translate("MainWindow", "Pippi Note"))
        self.checkBoxNPCSummoner_R.setText(_translate("MainWindow", "NPCSummoner"))
        self.checkBoxEasel_R.setText(_translate("MainWindow", "Easel"))
        self.checkBoxMusiqBox_R.setText(_translate("MainWindow", "MusiqBox"))
        self.checkBoxLazor_R.setText(_translate("MainWindow", "Lazor"))
        self.checkBoxCryptex_R.setText(_translate("MainWindow", "Cryptex"))
        self.checkBoxCheckpoint_R.setText(_translate("MainWindow", "Checkpoint"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Conan Exiles"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Extra"))
