"""Single Timer Tree implementation"""
from typing import List
import time

class ElapsedEntry(object):
    def __init__(self, start=None, stop=None):
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
            self.current_entry = ElapsedEntry(start=self.__class__.time_func())
            self.elapsed_entries.append(self.current_entry)
        
    def stop(self):
        if self.current_entry:
            res = self.current_entry
            self.current_entry.stop = self.__class__.time_func()
            self.current_entry = None
            return res
                
    def reset(self):
        res = self.stop()
        self.start()
        return res
