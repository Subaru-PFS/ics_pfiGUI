__author__ = 'alefur'

import sys
import os
import pwd
import argparse

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from mainwindow import PfiGUI


class pfiGUI(QMainWindow):
    def __init__(self, reactor, actor, d_width, d_height, cmdrName, systemPath):
        QMainWindow.__init__(self)
        self.reactor = reactor
        self.actor = actor
        self.display = d_width, d_height
        self.setName("%s.%s" % ("pfiGUI", cmdrName))
        self.systemPath = systemPath

        self.centWidget = PfiGUI(self)
        self.setCentralWidget(self.centWidget)

        self.show()

    def setName(self, name):
        self.cmdrName = name
        self.setWindowTitle(name)

    def closeEvent(self, QCloseEvent):
        self.reactor.callFromThread(self.reactor.stop)
        QCloseEvent.accept()


def main():
    app = QApplication(sys.argv)

    parser = argparse.ArgumentParser()

    parser.add_argument('--name', default=pwd.getpwuid(os.getuid()).pw_name, type=str, nargs='?', help='cmdr name')
    parser.add_argument('--stretch', default=0.6, type=float, nargs='?', help='window stretching factor')

    args = parser.parse_args()

    systemPath = '%s/%s' % (os.getcwd(), sys.argv[0].split('main.py')[0])
    geometry = app.desktop().screenGeometry()
    import qt5reactor

    qt5reactor.install()
    from twisted.internet import reactor

    import miniActor
    models = ['peb']
    actor = miniActor.connectActor(models)

    try:
        ex = pfiGUI(reactor,
                    actor,
                    geometry.width() * args.stretch,
                    geometry.height() * args.stretch,
                    args.name,
                    systemPath)
    except:
        actor.disconnectActor()
        raise

    reactor.run()
    actor.disconnectActor()


if __name__ == "__main__":
    main()
