# ComplexityScience Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (started 2026-10-21)

**Context:** ComplexityScience is a **self-study** workshop (GreenTeaPress Task 24): not offered live now, but the notebooks are maintained and run on Colab. Based on *Think Complexity*, 2nd edition. Guide: the "Refresh checklist" (self-study variant) in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are worked examples, and BayesianDecisionAnalysis is the self-study precedent. 40 stars. Given at PyCon US 2017 (with Jason Woodard), PyCon US 2018, and SciPy 2019; the most recent recording is [SciPy 2019](https://www.youtube.com/watch?v=ccA6ghSW1Iw).

**0. Set up**
- [x] `git fetch`/pull (1 README commit behind, fast-forwarded); uncommitted edits and untracked files decided (below)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-21), with `exclude:` in the root `_config.yml` because Pages serves `master` / with Jekyll
- [x] Tags (2026-10-21): `scipy-2019` at `8122b92` ("Fixing boundary", 2019-07-09 08:50 Austin time, the tutorial day; Allen chose it over `c45df1b`, 2019-05-23); `pre-refresh-2026` at `e64be01`. PyCon 2017 and 2018 predate the repo (first commit 2019-05-14), so no tags
- [x] README: each recording lists its tag (step 5)
- [x] Inventory (below)
- [x] Environment: `mamba env create -f environment.yml` (created as `ComplexityScience`, 2026-10-21: Python 3.13.16, NumPy 2.5, SciPy 1.18, Matplotlib 3.11, NetworkX 3.7, Seaborn 0.13, empiricaldist 0.10)

**1. Runs in a current environment**
- [x] `environment.yml` rewritten (2026-10-21): conda-forge, Python 3.13, Jupyter, NumPy, SciPy, Matplotlib, Seaborn, NetworkX (the `networkx=2.*` pin dropped), pytest, nbmake, the Jupyter Book tools, empiricaldist from pip. `requirements.txt` (unpinned; Colab lacks only empiricaldist) and `requirements-dev.txt` (adds Jupyter, pytest, nbmake)
- [x] Install/download cells: `03`'s old `IN_COLAB` / `!pip install` cell replaced by a try/import `%pip install -q empiricaldist` cell (the SurvivalAnalysisPython pattern) and moved to the first code cell. `01` needs nothing. The existing `download()` cells in `02` (helper scripts) and `03` (Facebook data) already skip files that exist and use absolute URLs; left where they are
- [x] Breakage and deprecation warnings: none. All three solutions run with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors (`01` 12 s, `02` 83 s (animations), `03` 11 s). The helper scripts (`Life.py`, `LifeRabbits.py`, `LifePuffer.py`) run with `-W error` too
- [x] `np.set_printoptions(legacy='1.25')` in the import cell of all six notebooks; re-ran the three solutions in place (no `np.float64(`/`np.int64(` in outputs). Student versions rebuilt from the solutions with `remove_soln.py`, which now also drops nbconvert's execution-timing metadata and execution counts (a rebuild before the edits reproduced the committed student versions exactly)
- [x] Data URLs: the four helper scripts and `facebook_combined.txt.gz` on `raw/master`, and the SNAP original, return 200
- [x] Replace Binder and Anaconda instructions in the README with Colab first, then pip or mamba (step 5)

**2. Tests and CI**
- [x] `pytest --nbmake soln/*.ipynb`: the three solutions pass. The student versions run too (their blanks are `# Solution goes here` comments; all three pass, 63 s), but CI runs only the solutions (Allen, 2026-10-21)
- [x] `.github/workflows/tests.yml` (push to `master`, PR, monthly, manual; Python 3.13; pip with `requirements-dev.txt`; 20-minute timeout; `actions/checkout@v5`, `actions/setup-python@v6`), 2026-10-21. First run passed in 2.5 min (3 passed in 100 s; run 39627213054). Annotation: `ubuntu-latest` moves to Ubuntu 26 from 2026-10-19 (informational)
- [x] Status badge in the README

**3. Colab**
- [x] "Click here to run this notebook on Colab" cell after the title of all six notebooks; solutions also link to the version with blanks (2026-10-21). `remove_soln.py` points the student version's cell at itself. README table: step 5
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [x] Typos and docstrings (2026-10-21, solutions, carried into the student versions by `remove_soln.py`): `01` missing closing quote after "Models of Segregation", "a visualization the grid", "Choose and unhappy agent", `grip:` → `grid:` (2 docstrings); `02` "Here's are", "blinkers, blocks, and beehives,", "natually", "Methuselas" (heading), "initial conditional run", "implementaion", "look up table"; `03` "intereted", "Facecook", "they is evidence", "random seen". Helper scripts: see Content issues 1–3. codespell's other hits are base64 image data or "still lifes" (the Life term)
- [x] Links: `thinkcomplex.com/schell` and Achim Flammenkamp's page http → https; NetworkX source link `blob/master` → `blob/main`; missing periods after two links. `thinkcomplex.com` short links kept (they redirect by design). Wikipedia links returned 429 (rate limit) from here, not checked
- [x] Notebook layout: H1 title plus one-line subtitle ("Examples and exercises for the tutorial [Complexity Science](…), based on *Think Complexity*, 2nd edition"), Colab cell, `##` sections (`01`'s second H1 "The Big Sort" → `##`); copyright (`01`, `02` "2019–2026"; `03` "2016–2026") and licenses (code MIT, text CC BY-NC-SA 4.0, Allen 2026-10-21) in a cell at the end, replacing the trailing empty code cell. All six notebooks validate; one ATX H1 each
- [x] Everything else under "Content issues" (items 1–7 decided and done, 2026-10-21)

**5. README in the standard shape**
- [x] README rewritten (2026-10-21): title, badge, author, self-study line, abstract (from the notebooks), *Think Complexity* 2e, hub link, level (introductory; basic Python, Allen), length (about 3 hours, Allen), outline, notebook table with Colab links, slides (link from Allen), recordings (SciPy 2019 with tag `scipy-2019`; PyCon US 2018, 2017), running instructions (Colab, pip, mamba), next steps, license (code MIT, text CC BY-NC-SA 4.0); `LICENSE` exists (MIT). Binder and Anaconda instructions dropped. All links return 200

**6. Site and visibility** (self-study; Allen chose a small Jupyter Book site on `gh-pages`, 2026-10-21)
- [ ] `jb/` from the BayesMadeSimple template: landing page plus the three solution notebooks
- [ ] SEO checklist in a scratch build; Allen reviews the descriptions
- [ ] Publish to `gh-pages`, switch Pages from `master` / to `gh-pages`, request a build, then delete the root `_config.yml`; check the live site; `robots.txt` sitemap line; Search Console; Task 22
- [ ] Hub entry; repo description and topics (add `jupyter-book`)

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

### Inventory (2026-10-21)

**Workshop notebooks** (solutions in `soln/`, saved with outputs; versions with blanks at the top level, no outputs; `build.sh` + `remove_soln.py` make the blank versions from the solutions):
- `01_workshop`: agent-based models of segregation (Schelling).
- `02_workshop`: Game of Life. Downloads `Cell2D.py`, `Life.py`, `LifeRabbits.py`, `LifePuffer.py` from `raw/master`.
- `03_workshop`: scale-free networks. Downloads `facebook_combined.txt.gz` from `raw/master` (original source: SNAP); old `IN_COLAB` / `!pip install empiricaldist` cell.

**Libraries:** NumPy, Matplotlib, Seaborn, SciPy, NetworkX, empiricaldist.

**Helpers:** `Cell2D.py`, `Life.py`, `LifeRabbits.py`, `LifePuffer.py` (used by `02`).

**Other files:** `environment.yml` (Python 3.7, `networkx=2.*`), `_config.yml` (Jekyll minimal theme), `LICENSE` (MIT), `build.sh`, `remove_soln.py`.

**Decisions on local state (Allen, 2026-10-21):**
- Uncommitted `Cell2D.py` edit (unused imports dropped, class docstring "Parent class for 2-D cellular automata"): committed.
- `.ipynb_checkpoints/` (root and `soln/`): deleted, backed up to the session scratchpad.
- `utils.py` (not used by any notebook): deleted; it stays in the tags and history.
- Untracked copies in `soln/` (`Cell2D.py` (old version), `Life.py`, `LifeRabbits.py`, `facebook_combined.txt.gz`; downloaded when running the solutions there): left in place.

### Content issues

(For Allen to decide.)

1. ~~`02` says to run `LifeRabbits.py` and `LifePuffer.py` "in a terminal", which Colab users can't do.~~ Allen (2026-10-21): keep the instructions and say they need a local install. Done: "This needs a local installation of Python; it doesn't work on Colab." in both cells.
2. ~~`Cell2D.py` and `Life.py` docstrings tell readers to install ffmpeg for animation in the notebook.~~ Allen (2026-10-21): removed (the notebooks animate with `clear_output`; commit "Don't need ffmpeg any more", 2019).
3. ~~Helper scripts say "Complexity and Computation" and link `http://greenteapress.com/complexity`.~~ Allen (2026-10-21): now *Think Complexity*, 2nd edition, `https://thinkcomplex.com`; MIT link → `https://opensource.org/license/MIT`. The dead rabbits link in `LifeRabbits.py` now points to the same web.archive.org copy the notebook uses.
4. ~~`03`, the cell before the friends plots: "I'll use `EstimatedPdf`, which computes a smooth Probability Density Function", but the code uses `Pmf.from_seq(...).plot()`.~~ Allen (2026-10-21): now "To plot the degree distribution, I'll use `Pmf`."
5. ~~`03`, "Cumulative distributions": "the Facebook data, the WS model, and the BA model", but this notebook has no WS model.~~ Allen (2026-10-21): "the WS model" dropped.
6. ~~`01`, The Big Sort: the exercise template is `step(grid, num_comps=2)`, but the solution is `step(grid)` with `num_comps = 2` hard-coded (its docstring still lists `num_comps`), so the next exercise ("Experiment with different values of `num_comps`") needs an edit inside the function.~~ Allen (2026-10-21): the solution is now `step(grid, num_comps=2)`, hard-coded line removed.
7. ~~`03` has a commented-out cell that silenced `mplDeprecation` warnings (`matplotlib.cbook.mplDeprecation` no longer exists); dead code.~~ Allen (2026-10-21): cell deleted.
