__author__ = 'alefur'

from datetime import datetime as dt
from functools import partial

from PyQt5.QtWidgets import QGridLayout, QWidget, QGroupBox, QLineEdit, QPushButton, QPlainTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QTextCursor

from widgets import ValueGB, LeakageBox, PowerButton, ResetButton
from graph import Graph, Curve


class LogArea(QPlainTextEdit):
    def __init__(self):
        QPlainTextEdit.__init__(self)
        self.logArea = QPlainTextEdit()
        self.setMaximumBlockCount(10000)
        self.setReadOnly(True)

        self.setStyleSheet("background-color: black;color:white;")
        self.setFont(QFont("Monospace", 8))

    def newLine(self, line):
        self.insertPlainText("\n%s  %s" % (dt.now().strftime("%H:%M:%S.%f"), line))
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

    def trick(self, qlineedit):
        self.newLine(qlineedit.text())


class PfiGUI(QWidget):
    def __init__(self, mainTree):
        QWidget.__init__(self)
        self.mainTree = mainTree
        self.mainLayout = QGridLayout()
        self.windowLayout = QHBoxLayout()
        self.labelLayout = QGridLayout()

        self.labelLayout.addWidget(ValueGB('AGC-4(C) ', self.actor.models['peb'], 'temps', 0, '{:g}'), 0, 0)
        self.labelLayout.addWidget(ValueGB('AGC-3(C) ', self.actor.models['peb'], 'temps', 1, '{:g}'), 0, 1)
        self.labelLayout.addWidget(ValueGB('AGC-2(C) ', self.actor.models['peb'], 'temps', 2, '{:g}'), 0, 2)
        self.labelLayout.addWidget(ValueGB('AGC-1(C) ', self.actor.models['peb'], 'temps', 3, '{:g}'), 0, 3)
        self.labelLayout.addWidget(ValueGB('AGC-6(C) ', self.actor.models['peb'], 'temps', 4, '{:g}'), 0, 4)
        self.labelLayout.addWidget(ValueGB('AGC-5(C) ', self.actor.models['peb'], 'temps', 5, '{:g}'), 0, 5)
        self.labelLayout.addWidget(ValueGB('UL Link-1(C) ', self.actor.models['peb'], 'temps', 6, '{:g}'), 0, 6)
        self.labelLayout.addWidget(ValueGB('UL Link-2(C) ', self.actor.models['peb'], 'temps', 7, '{:g}'), 1, 0)
        self.labelLayout.addWidget(ValueGB('UL Link-3(C) ', self.actor.models['peb'], 'temps', 8, '{:g}'), 1, 1)
        self.labelLayout.addWidget(ValueGB('Positioner Frame(C) ', self.actor.models['peb'], 'temps', 9, '{:g}'), 1, 2)
        self.labelLayout.addWidget(ValueGB('COB-1(C) ', self.actor.models['peb'], 'temps', 10, '{:g}'), 1, 3)
        self.labelLayout.addWidget(ValueGB('COB-2(C) ', self.actor.models['peb'], 'temps', 11, '{:g}'), 1, 4)
        self.labelLayout.addWidget(ValueGB('COB-3(C) ', self.actor.models['peb'], 'temps', 12, '{:g}'), 1, 5)
        self.labelLayout.addWidget(ValueGB('COB-4(C) ', self.actor.models['peb'], 'temps', 13, '{:g}'), 1, 6)
        self.labelLayout.addWidget(ValueGB('COB-5(C) ', self.actor.models['peb'], 'temps', 14, '{:g}'), 2, 0)
        self.labelLayout.addWidget(ValueGB('COB-6(C) ', self.actor.models['peb'], 'temps', 15, '{:g}'), 2, 1)
        self.labelLayout.addWidget(ValueGB('EBOX-1(C) ', self.actor.models['peb'], 'temps', 16, '{:g}'), 2, 2)
        self.labelLayout.addWidget(ValueGB('EBOX-2(C) ', self.actor.models['peb'], 'temps', 17, '{:g}'), 2, 3)
        self.labelLayout.addWidget(ValueGB('EBOX-3(C) ', self.actor.models['peb'], 'temps', 18, '{:g}'), 2, 4)
        self.labelLayout.addWidget(ValueGB('Flow in(C) ', self.actor.models['peb'], 'temps', 19, '{:g}'), 2, 5)
        self.labelLayout.addWidget(ValueGB('Flow out(C) ', self.actor.models['peb'], 'temps', 20, '{:g}'), 2, 6)
        self.labelLayout.addWidget(ValueGB('Humidity ', self.actor.models['peb'], 'humidity', 0, '{:g}'), 3, 0)
        self.labelLayout.addWidget(ValueGB('Temperature(C) ', self.actor.models['peb'], 'humidity', 1, '{:g}'), 3, 1)
        self.labelLayout.addWidget(ValueGB('Dew Point(C) ', self.actor.models['peb'], 'humidity', 2, '{:g}'), 3, 2)
        self.labelLayout.addWidget(ValueGB('Flow meter ', self.actor.models['peb'], 'flow', 0, '{:g}'), 3, 4)
        self.labelLayout.addWidget(LeakageBox('Leakage ', self.actor.models['peb'], 'leakage', 0, '{:g}'), 3, 5)
        self.labelLayout.addWidget(LeakageBox('Disconnect ', self.actor.models['peb'], 'leakage', 1, '{:g}'), 3, 6)
        self.labelLayout.addWidget(self.createButton(title='All AGC ON', cmdStr='peb power on agc'), 4, 0)
        self.labelLayout.addWidget(PowerButton('AGC-1 ', self.actor.models['peb'], 'power', 0, self.sendCommand, 'peb power on agc ids=1', 'peb power off agc ids=1'), 4, 1, 2, 1)
        self.labelLayout.addWidget(PowerButton('AGC-2 ', self.actor.models['peb'], 'power', 1, self.sendCommand, 'peb power on agc ids=2', 'peb power off agc ids=2'), 4, 2, 2, 1)
        self.labelLayout.addWidget(PowerButton('AGC-3 ', self.actor.models['peb'], 'power', 2, self.sendCommand, 'peb power on agc ids=3', 'peb power off agc ids=3'), 4, 3, 2, 1)
        self.labelLayout.addWidget(PowerButton('AGC-4 ', self.actor.models['peb'], 'power', 3, self.sendCommand, 'peb power on agc ids=4', 'peb power off agc ids=4'), 4, 4, 2, 1)
        self.labelLayout.addWidget(PowerButton('AGC-5 ', self.actor.models['peb'], 'power', 4, self.sendCommand, 'peb power on agc ids=5', 'peb power off agc ids=5'), 4, 5, 2, 1)
        self.labelLayout.addWidget(PowerButton('AGC-6 ', self.actor.models['peb'], 'power', 5, self.sendCommand, 'peb power on agc ids=6', 'peb power off agc ids=6'), 4, 6, 2, 1)
        self.labelLayout.addWidget(self.createButton(title='All AGC OFF', cmdStr='peb power off agc'), 5, 0)
        self.labelLayout.addWidget(ValueGB('Led period(us) ', self.actor.models['peb'], 'ledperiod', 0, '{:g}'), 6, 0)
        self.labelLayout.addWidget(ValueGB('Led dutycycle(%) ', self.actor.models['peb'], 'dutycycle', 0, '{:g}'), 6, 1)
        self.labelLayout.addWidget(self.createButton(title='LED ON', cmdStr='peb led on'), 6, 3)
        self.labelLayout.addWidget(self.createButton(title='LED FLASH', cmdStr='peb led flash'), 6, 4)
        self.labelLayout.addWidget(self.createButton(title='LED OFF', cmdStr='peb led off'), 6, 5)
        self.labelLayout.addWidget(PowerButton('Leakage ', self.actor.models['peb'], 'power', 6, self.sendCommand, 'peb power on leakage', 'peb power off leakage'), 7, 0, 2, 1)
        self.labelLayout.addWidget(PowerButton('Adam6015 ', self.actor.models['peb'], 'power', 7, self.sendCommand, 'peb power on adam', 'peb power off adam'), 7, 1, 2, 1)
        self.labelLayout.addWidget(PowerButton('USB-1 ', self.actor.models['peb'], 'power', 10, self.sendCommand, 'peb power on usb ids=1', 'peb power off usb ids=1'), 7, 2, 2, 1)
        self.labelLayout.addWidget(PowerButton('USB-2 ', self.actor.models['peb'], 'power', 11, self.sendCommand, 'peb power on usb ids=2', 'peb power off usb ids=2'), 7, 3, 2, 1)
        self.labelLayout.addWidget(ResetButton('Flow Board ', self.actor.models['peb'], 'power', 8, self.sendCommand, 'peb power bounce boardb'), 7, 4, 2, 1)
        self.labelLayout.addWidget(ResetButton('LED Board ', self.actor.models['peb'], 'power', 9, self.sendCommand, 'peb power bounce boardc'), 7, 5, 2, 1)
        self.labelLayout.addWidget(ResetButton('Switch ', self.actor.models['peb'], 'power', 12, self.sendCommand, 'peb power bounce switch'), 7, 6, 2, 1)

        self.commandLine = QLineEdit()
        self.commandButton = QPushButton('Send Command')
        self.commandButton.clicked.connect(self.sendCmdLine)

        self.logArea = LogArea()

        self.mainLayout.addLayout(self.labelLayout, 0, 0, 1, 7)


        self.mainLayout.addWidget(self.commandLine, 2, 0, 1, 5)
        self.mainLayout.addWidget(self.commandButton, 2, 5, 1, 2)

        self.mainLayout.addWidget(self.logArea, 3, 0, 1, 7)
        self.setLayout(self.mainLayout)

    @property
    def actor(self):
        return self.mainTree.actor

    def createButton(self, title, cmdStr):
        button = QPushButton(title)
        button.clicked.connect(partial(self.sendCommand, cmdStr))
        return button

    def sendCmdLine(self):
         self.sendCommand(self.commandLine.text())

    def sendCommand(self, fullCmd):
        import opscore.actor.keyvar as keyvar
        [actor, cmdStr] =fullCmd.split(' ', 1)
        self.logArea.newLine('cmdIn=%s %s' % (actor, cmdStr))
        self.actor.cmdr.bgCall(**dict(actor=actor,
                                      cmdStr=cmdStr,
                                      timeLim=600,
                                      callFunc=self.returnFunc,
                                      callCodes=keyvar.AllCodes))

    def returnFunc(self, cmdVar):
        self.logArea.newLine('cmdOut=%s' % cmdVar.replyList[0].canonical())
        for i in range(len(cmdVar.replyList)-1):
            self.logArea.newLine(cmdVar.replyList[i+1].canonical())
