from gtts import gTTS
from time import sleep
import os
import pyglet


class FileCannotPlayError(Exception):
    def __init__(self, message="Due to Internet connection, we cannot speak out NLG output."):
        self.message = message
        super().__init__(self.message)


class T2SDefault:
    def __init__(self):
        self.tmp = 'tmp.mp3'

    def play(self, s: str):
        try:
            tts = gTTS(text=s, lang='en')
            filename = 'temp.mp3'
            tts.save(filename)
        except Exception as e:
            os.remove(filename)
            raise FileCannotPlayError()


        music = pyglet.media.load(filename, streaming=False)
        music.play()

        sleep(music.duration)
        os.remove(filename)
