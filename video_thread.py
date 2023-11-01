"""
doc
"""
import os
import threading
import pyttsx3
class video_class(threading.Thread):
    """
    doc
    """
    def __init__(self, audio_path, image_path):
        threading.Thread.__init__(self)
        self.audio_path = audio_path
        self.image_path = image_path
    def run(self):
        """
        doc
        """
        os.system("python video_maker.py --audio_path "+self.audio_path+ " --img_path "+self.image_path)
