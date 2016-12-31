import pyqtgraph
from PyQt4 import QtGui
from PyQt4 import QtCore


class LiveWire():
    def __init__(self):
        self.imgData = []
        self.imgWidth = 0
        self.imgHeight = 0


class LiveWireDemoGui(QtGui.QDialog):
    def __init__(self):
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.fileNameLabel = QtGui.QLabel("File name:")

def main():
    print 'Live wire demo'
    app = QtGui.QApplication("Live wire demo")
    mainWnd = LiveWireDemoGui()
    mainWnd.show()
    app.exec_()

if __name__ == '__main__':
    main()
