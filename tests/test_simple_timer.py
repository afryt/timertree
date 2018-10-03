import pytest
import os
import sys
import time
sys.path.append(os.path.join(os.path.abspath(__file__), '..'))

from timertree.timer import TimerTree

def test_simple_timer():
    duration = 1.23
    timer = TimerTree(name='SampleTimer')
    timer.start()
    time.sleep(duration)
    res = timer.stop()
    print(res.elapsed)
    assert abs(res.elapsed - duration) < 1e-2

