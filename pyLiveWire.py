import sys
import pyqtgraph
from PyQt4 import QtGui, QtCore, uic


class LiveWire():
    def __init__(self):
        self.imgData = []
        self.imgWidth = 0
        self.imgHeight = 0


class LiveWireDemoGui(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = uic.loadUi('pylivewire.ui')
        self.ui.show()

def main():
    print 'Live wire demo'
    app = QtGui.QApplication(sys.argv)
    window = LiveWireDemoGui()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
