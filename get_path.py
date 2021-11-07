import sys
import os

def get_path(myPath):
    try:
        def_path = sys._MEIPASS
    except Exception:
        def_path = os.path.abspath(".")
    return os.path.join(def_path, myPath)
