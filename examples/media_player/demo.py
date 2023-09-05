# coding: utf-8
import sys
from pathlib import Path

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene

from qfluentwidgets import SimpleMediaPlayBar, setTheme, Theme, StandardMediaPlayBar, VideoWidget


class Demo1(QWidget):

    def __init__(self):
        super().__init__()
        setTheme(Theme.DARK)
        self.vBoxLayout = QVBoxLayout(self)
        self.resize(500, 300)

        # self.player = QMediaPlayer(self)
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        # self.player.setPosition()

        self.simplePlayBar = SimpleMediaPlayBar(self)
        self.standardPlayBar = StandardMediaPlayBar(self)

        self.vBoxLayout.addWidget(self.simplePlayBar)
        self.vBoxLayout.addWidget(self.standardPlayBar)

        # online music
        url = QUrl("https://files.cnblogs.com/files/blogs/677826/beat.zip?t=1693900324")
        self.simplePlayBar.player.setSource(url)

        # local music
        url = QUrl.fromLocalFile(str(Path('resource/aiko - シアワセ.mp3').absolute()))
        self.standardPlayBar.player.setSource(url)

        # self.standardPlayBar.play()


class Demo2(QWidget):

    def __init__(self):
        super().__init__()
        self.vBoxLayout = QVBoxLayout(self)
        self.videoWidget = VideoWidget(self)

        self.videoWidget.setVideo(QUrl(
            'https://mvwebfs.tx.kugou.com/202309051557/028d27cbe9d79ae1ffafd9748df93090/v2/e7844104727ea50f658319f2723b6243/KGTX/CLTX002/e7844104727ea50f658319f2723b6243.mp4'))
        self.videoWidget.play()

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.videoWidget)
        self.resize(800, 450)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication([])
    demo1 = Demo1()
    demo1.show()
    demo2 = Demo2()
    demo2.show()
    sys.exit(app.exec())