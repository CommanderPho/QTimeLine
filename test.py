
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint, QLine, QRect, QRectF, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPalette, QPen, QPolygon, QPainterPath, QPixmap
from PyQt5.QtWidgets import QWidget, QFrame, QScrollArea, QVBoxLayout
import sys
import os
from qtimeline import QTimeLine

if __name__ == '__main__':
    shouldShowGUIWindows = True
    if (shouldShowGUIWindows):
        # create the application and the main window
        app = QtWidgets.QApplication( sys.argv )

        # mainWindow = EventsDrawingWindow(videoEvents, earliestTime, latestTime, dateTimes[relevant_labjack_indicies], dataArray[relevant_labjack_indicies] )
        mainWindow =  QTimeLine(360, 900) # Creates an 360/60 = 6 minutes long timeline
        desktop = QtWidgets.QApplication.desktop()
        resolution = desktop.availableGeometry()

        # Style
        app.setStyleSheet(
            "QToolTip { border: 2px solid darkkhaki; padding: 5px; border-radius: 3px; background-color: rgba(255,255,0,0); }");

        # run
        mainWindow.show()
        sys.exit( app.exec_() )