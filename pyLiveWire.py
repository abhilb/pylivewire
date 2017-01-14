import sys
import pyqtgraph as pg
import numpy as np
from PyQt4 import QtGui, uic


class LiveWire:
    """
    Implements the live wire algorithm.
    """

    def __init__(self):
        self.imgData = None

    def get_image(self):
        return self.imgData

    def set_image(self):
        data = np.random.normal(size=(200, 100))
        data[20:80, 20:80] += 2.
        data = pg.gaussianFilter(data, (3, 3))
        data += np.random.normal(size=(200, 100)) * 0.1
        self.imgData = data


class LiveWireDemoGui(QtGui.QWidget):
    """
    Implements the user interface for the live wire demo.
    """
    def __init__(self):
        QtGui.QWidget.__init__(self)
        uic.loadUi('pylivewire.ui', self)

        # Setting up the image display
        self.viewBox = pg.ViewBox()
        self.imgView.setCentralItem(self.viewBox)
        self.viewBox.setAspectLocked()
        self.imgItem = pg.ImageItem()
        self.viewBox.addItem(self.imgItem)

        self.liveWire = LiveWire()
        self.liveWire.set_image()
        self.imgItem.setImage(self.liveWire.get_image())


def main():
    app = QtGui.QApplication(sys.argv)
    window = LiveWireDemoGui()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
