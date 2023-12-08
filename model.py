import re
from tkinter import filedialog as fd
from os import path
from pydub import AudioSegment
from scipy.io import wavfile
import scipy.io


class Model:
    def __init__(self, filepath):
        self.filepath = filepath

        # use property decorator to use getters & setters
        # define email an attribute of Model
    @property
    def filepath(self):
        return self.__filepath

    @filepath.setter
    def filepath(self, value):
        """
        :param value:
        :return:
        """

        self.__filepath = value


    def import_wav(self):
        """
        Save the email into a file
        :return:
        """

        filetypes = (
            ('Waveform audio', '*.wav'),
            ('MP3 - requires conversion', '*.mp3'),
            ('All files', '*.*')
        )

        filepath = fd.askopenfilename(
            title='Choose file to import',
            initialdir='/',
            filetypes=filetypes
        )

        if filepath.endswith('.wav'):
            wav = AudioSegment.from_file(filepath, format="wav")
        elif filepath.endswith('.mp3'):
            wav = AudioSegment.from_mp3(filepath)
        else:
            raise ValueError(f'Unsupported file type: {filepath}')

        self.filepath = filepath

        wav.tags = None
        wav.set_channels(1)
        wav.export("acoustics,wav", format="wav")


