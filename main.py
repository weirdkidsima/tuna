import tkinter
import tkinter.messagebox
import os
import sys
import json
import requests
import webbrowser
import time
import numpy as np
import random
from distutils.version import StrictVersion as Version

from audio.analyzer import AudioAnalyzer
from audio.helper import ProtectedList
from audio.thread import SoundThread