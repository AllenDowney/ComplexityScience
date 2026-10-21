# ComplexityScience

Allen Downey's tutorial on complexity science, based on *Think Complexity*, 2nd edition: agent-based models (Schelling segregation), the Game of Life, and scale-free networks, in Python. Given at PyCon US 2017 (with Jason Woodard), PyCon US 2018, and SciPy 2019. Self-study material now: not offered live, but the notebooks are maintained and run on Colab. The GitHub Pages site (`allendowney.github.io/ComplexityScience/`) is the Jupyter Book in `jb/`, published to the `gh-pages` branch: a landing page and the three solution notebooks.

**Guide for the 2026 refresh:** the "Refresh checklist" (self-study variant) in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple and CompStats are worked examples). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

Student versions (with blanks) are at the top level; solutions are in `soln/` under the same names.

- `01_workshop.ipynb`: Schelling's model of segregation.
- `02_workshop.ipynb`: Game of Life (uses `Cell2D.py`, `Life.py`, `LifeRabbits.py`, `LifePuffer.py`).
- `03_workshop.ipynb`: scale-free networks (uses `facebook_combined.txt.gz` and empiricaldist).

The notebooks download the helper and data files from raw URLs on `master`, so keep those files at the top level and don't rename the branch.

Edit the solutions in `soln/`; `build.sh <notebooks>` copies them up and runs `remove_soln.py` to make the student versions (cells starting with `# Solution` are blanked, outputs and tags cleared).

## Site

`jb/` builds the Jupyter Book site (`cd jb; ./build.sh [publish]`); `prep_notebooks.py` copies the solution notebooks in as `segregation`, `game_of_life`, and `scale_free_networks`, and holds the page descriptions. Template: BayesMadeSimple. Delete an old `jb/_build/` before publishing (`jb build` doesn't clean it).

## Tags

- `scipy-2019`: the code in the SciPy 2019 video.
- `pre-refresh-2026`: the state before the 2026 refresh.
- `2026-refresh`: the refreshed version (Python 3.13, 2026-10-21).

## Testing

Environment: `mamba env create -f environment.yml` (name `ComplexityScience`). Run the solutions top to bottom:

```
pytest --nbmake soln/*.ipynb
```

The target environment is Google Colab's current Python and libraries.

## Conventions

- Branch is `master`; keep it.
- Don't change the substance of the text; list content questions under "Content issues" on the board for Allen to decide.
- Keep student and solution versions in sync: same cells, solutions replaced by blanks.
- Pages serves `gh-pages`, so committed `.md` files on `master` are not published.
