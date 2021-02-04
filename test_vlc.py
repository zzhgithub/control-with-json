import vlc
import time
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMacCocoaViewContainer
from scheduler_composer import SchedulerComposer
from scheduler_builder import build

scheduler_composer = SchedulerComposer()


class SigSlot(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('XXOO')

        vbox = QVBoxLayout()
        self.wv = QMacCocoaViewContainer(0)
        vbox.addWidget(self.wv)
        self.setLayout(vbox)
        self.resize(350, 250)

    def bind(self, player):
        player.set_nsobject(int(self.wv.winId()))


if __name__ == '__main__':
    media_player: vlc.MediaPlayer = vlc.MediaPlayer()
    mrl = "test.mp4"
    media_player.set_mrl(mrl)

    vlcApp = QApplication(sys.argv)
    sip = SigSlot()
    sip.bind(media_player)
    sip.show()

    time.sleep(5)
    media_player.play()
    filename = "example.json"
    schedule = build(filename)
    scheduler_composer.add(filename, schedule)
    schedule.start()

    # getting width at index 0
    value = media_player.video_get_width(0)

    # printing width
    print("Width at Index 0 : ")
    print(value)

    sys.exit(vlcApp.exec_())
