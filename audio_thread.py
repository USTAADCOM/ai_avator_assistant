"""
doc
"""
import threading
import pyttsx3
class voice_class(threading.Thread):
    """
    doc
    """
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text
    def run(self):
        """
        doc
        """
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume',1.0)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(self.text)
        engine.runAndWait()
        engine.stop()
        engine.save_to_file(self.text, 'female.wav')
        engine.runAndWait()
