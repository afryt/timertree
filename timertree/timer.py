"""Single Timer Tree implementation"""
from typing import List
import time

class ElapsedEntry(object):
    def __init__(self, start=None, stop=None):
        self.start = start
        self.stop = stop
    
    @property
    def elapsed(self):
        return self.stop - self.start

"""
ElapsedEntry should have nested children, so as to create Tree structure.
Currently it won't work because when children add entries those won't be tied to a given entry in the parent.
"""

class TimerTree(object):
    time_func = time.time
    def __init__(self, name : str, parent = None, report_type='summary'):
        self.children : List[TimerTree] = []
        self.name : str = name
        self.parent : TimerTree = parent
        self.elapsed_entries : List[ElapsedEntry] = []
        self.current_entry : ElapsedEntry = None
        self.report_type = report_type  # used to determine if summarize all elapsed entries
        if parent:
            self.parent.children.append(self)

    def start(self):
        if not self.current_entry:
            self.current_entry = ElapsedEntry(start=self.__class__.time_func())
            self.elapsed_entries.append(self.current_entry)
        
    def stop(self) -> ElapsedEntry:
        if self.current_entry:
            res = self.current_entry
            self.current_entry.stop = self.__class__.time_func()
            self.current_entry = None
            self.elapsed_entries.append(res)        # store it for reporting purposes
            return res
                
    def reset(self) -> ElapsedEntry:
        res = self.stop()
        self.start()
        return res

    def summary(self, depth=-1):
        
        pass