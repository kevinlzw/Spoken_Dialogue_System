import speech_recognition as sr


class ASRDefault:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source, timeout=10, phrase_time_limit=10)
        try:
            response = self.r.recognize_google(audio)
        except:
            response = self.r.recognize_sphinx(audio)
        return response
