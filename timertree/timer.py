"""Single Timer Tree implementation"""
from typing import List
import time

class ElapsedEntry(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class TimerTree(object):
    time_func = time.time
    def __init__(self, name : str, parent : TimerTree = None):
        self.name : str = name
        self.parent : TimerTree = parent
        self.elapsed_entries : List[ElapsedEntry] = []
        self.current_entry : ElapsedEntry = None

    def start(self):
        if not self.current_entry:
            self.current_entry