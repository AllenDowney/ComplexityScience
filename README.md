# Complexity Science

[![tests](https://github.com/AllenDowney/ComplexityScience/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/ComplexityScience/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

This is self-study material: the workshop is not offered live now, but the notebooks are maintained and run on Colab.

This tutorial is a hands-on introduction to complexity science, using Python to build and explore simple models that produce surprisingly complex behavior. We start with agent-based models: Schelling's model of segregation, and a variation based on Bill Bishop's *The Big Sort*. Then we explore cellular automata with Conway's Game of Life, including still lifes, oscillators, spaceships, Methuselahs, and the glider gun, and see how to implement it efficiently with NumPy and SciPy. Finally, we use NetworkX to analyze the degree distribution of a Facebook social network, look at power laws and the friendship paradox, and compare the data with the Barabási–Albert model. For each part, there is a Jupyter notebook where you can run the code and work on exercises.

The examples in this tutorial are from my book, [*Think Complexity*, 2nd edition](https://greenteapress.com/wp/think-complexity-2e/), and a class I taught at Olin College.

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).

**Level:** introductory. You should be familiar with basic Python and Jupyter notebooks; some experience with NumPy helps. You don't need to know anything about complexity science.

**Length:** about 3 hours.

## Outline

1. **Agent-based models of segregation:** Schelling's model, implemented with NumPy arrays and 2-D correlation; then the Big Sort, where agents choose neighborhoods with people like themselves.
2. **Game of Life:** still lifes, oscillators, and spaceships; Methuselahs; Conway's conjecture, the glider gun, and the puffer train; an efficient implementation with correlation and a lookup table; and Highlife, a variation with one more rule.
3. **Scale-free networks:** graphs with NetworkX; the degree distribution of a Facebook network; the friendship paradox; power law distributions; and the Barabási–Albert model.

Each notebook comes in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| 1. Agent Based Models of Segregation | [Run on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/01_workshop.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/soln/01_workshop.ipynb) |
| 2. Game of Life | [Run on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/02_workshop.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/soln/02_workshop.ipynb) |
| 3. Scale-Free Networks | [Run on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/03_workshop.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/soln/03_workshop.ipynb) |

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vRccKWgJoVoU_VYIh80LyVeLOy-j6DmMVPACFW0Owm5mtXDt4n0p-zcSZzeSYW-vxZOP3thY_AOQjgb/pub?start=false&loop=false&delayms=3000).

## Recordings

I presented this tutorial at PyCon US 2017 (with Jason Woodard), PyCon US 2018, and SciPy 2019. The code in the videos is not the current version; the tag after the SciPy link is the version of the code that goes with it. The PyCon tutorials predate this repository.

* [SciPy 2019](https://www.youtube.com/watch?v=ccA6ghSW1Iw): tag [`scipy-2019`](https://github.com/AllenDowney/ComplexityScience/tree/scipy-2019)
* [PyCon US 2018](https://www.youtube.com/watch?v=F0uiLhZmtN4)
* [PyCon US 2017](https://www.youtube.com/watch?v=qHWhy3PWhes)

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, SciPy, Matplotlib, Seaborn, NetworkX, and [empiricaldist](https://pypi.org/project/empiricaldist/). You can [download the code in this zip file](https://github.com/AllenDowney/ComplexityScience/archive/master.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/ComplexityScience
cd ComplexityScience
```

Then install the packages with pip:

```
pip install -r requirements.txt
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate ComplexityScience
```

Then run `jupyter lab` and open `01_workshop.ipynb`.

The Game of Life notebook also mentions two scripts, `LifeRabbits.py` and `LifePuffer.py`, that run longer animations in a window; they need a local installation.

## Next steps

To go further, read [*Think Complexity*, 2nd edition](https://greenteapress.com/wp/think-complexity-2e/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
