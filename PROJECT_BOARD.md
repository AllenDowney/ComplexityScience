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
- [ ] README: each recording lists its tag (step 5)
- [x] Inventory (below)
- [ ] Environment: `mamba env create -f environment.yml` (after `environment.yml` is rewritten in step 1)

**1. Runs in a current environment**
- [ ] `environment.yml` (conda-forge, Python 3.13, pytest, nbmake, site build tools), `requirements.txt`, `requirements-dev.txt`
- [ ] Install/download cell in each notebook (empiricaldist in `03`; helpers in `02`; data in `03`)
- [ ] Breakage and deprecation warnings (NumPy 2, SciPy, Matplotlib, NetworkX 3, Seaborn)
- [ ] `np.set_printoptions(legacy='1.25')` in the import cell; re-run the solutions saved with outputs
- [ ] Data URLs (helpers and `facebook_combined.txt.gz` come from raw files on `master`)
- [ ] Replace Binder and Anaconda instructions in the README with Colab first, then pip or mamba (step 5)

**2. Tests and CI**
- [ ] `pytest --nbmake` on the solutions (and the versions with blanks, if they run)
- [ ] `.github/workflows/tests.yml`; watch the first run
- [ ] Status badge in the README

**3. Colab**
- [ ] "Click here to run this notebook on Colab" cell after the title of each notebook; solutions also link to the version with blanks; Colab links in the README
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos, wrong docstrings, broken links (http → https)
- [ ] Notebook layout: H1 title, Colab cell, `##` sections, copyright ("2016–2026" / "2019–2026") and licenses (code MIT, text CC) at the end; same in student and solution versions
- [ ] Everything else under "Content issues"

**5. README in the standard shape**
- [ ] Title, badge, author, self-study line, abstract, level, length (ask Allen), outline, notebook table with Colab links, slides, recordings with tags, running instructions, next steps (*Think Complexity*, hub), license; `LICENSE` exists (MIT)

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
