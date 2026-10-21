"""Copy the solution notebooks into jb/ and prepare them for the book.

Writes segregation.ipynb, game_of_life.ipynb, and scale_free_networks.ipynb here
from ../soln/0*_workshop.ipynb (named by topic for clean URLs). Each notebook already
has its own H1 and `##` sections, so only the page description is added, in the
notebook metadata (see GreenTeaPress plans/seo.md).
"""

import nbformat

PAGES = {
    'segregation': (
        '01_workshop',
        "Agent-based models in Python: implement Schelling's model of segregation with "
        "NumPy and 2-D correlation, then a variation based on The Big Sort.",
    ),
    'game_of_life': (
        '02_workshop',
        "Conway's Game of Life in Python: still lifes, oscillators, gliders, Methuselahs, "
        "and the glider gun, with a fast NumPy and SciPy implementation.",
    ),
    'scale_free_networks': (
        '03_workshop',
        "Scale-free networks in Python: the degree distribution of a Facebook network, "
        "the friendship paradox, power laws, and the Barabási–Albert model.",
    ),
}


def prepare(name, source, description):
    nb = nbformat.read(f'../soln/{source}.ipynb', nbformat.NO_CONVERT)

    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name}: {nb.cells[0].source.splitlines()[0]} ({len(description)} characters)')


for name, (source, description) in PAGES.items():
    prepare(name, source, description)
