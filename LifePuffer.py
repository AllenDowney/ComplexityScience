""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2016 Allen Downey
MIT License: http://opensource.org/licenses/MIT
"""
from __future__ import print_function, division

import sys
import matplotlib.pyplot as plt

from Life import Life, LifeViewer

def main(script, *args):
    """Constructs a puffer train.

    Uses the entities in this file:
    http://www.radicaleye.com/lifepage/patterns/puftrain.lif
    """
    lwss = [
        '0001',
        '00001',
        '10001',
        '01111'
    ]

    bhep = [
        '1',
        '011',
        '001',
        '001',
        '01'
    ]

    n = 400
    m = 600
    life = Life(n, m)

    col = 120
    life.add_cells(n//2+12, col, *lwss)
    life.add_cells(n//2+26, col, *lwss)
    life.add_cells(n//2+19, col, *bhep)
    viewer = LifeViewer(life)
    anim = viewer.animate(frames=100, interval=1)
    plt.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)
    plt.show()


if __name__ == '__main__':
    main(*sys.argv)


