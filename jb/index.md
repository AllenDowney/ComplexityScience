---
myst:
  html_meta:
    description: "A hands-on Python tutorial on complexity science: Schelling's segregation model, Conway's Game of Life, and scale-free networks, from Think Complexity."
og:description: "A hands-on Python tutorial on complexity science: Schelling's segregation model, Conway's Game of Life, and scale-free networks, from Think Complexity."
---

# Complexity Science: A Tutorial in Python

[Allen Downey](https://allendowney.com)

This is self-study material: the workshop is not offered live now, but the notebooks are maintained and run on Colab.

This tutorial is a hands-on introduction to complexity science, using Python to build and explore simple models that produce surprisingly complex behavior. We start with agent-based models: Schelling's model of segregation, and a variation based on Bill Bishop's *The Big Sort*. Then we explore cellular automata with Conway's Game of Life, and see how to implement it efficiently with NumPy and SciPy. Finally, we use NetworkX to analyze the degree distribution of a Facebook social network, look at power laws and the friendship paradox, and compare the data with the Barabási–Albert model.

The examples in this tutorial are from my book, [*Think Complexity*, 2nd edition](https://allendowney.github.io/ThinkComplexity2/), and a class I taught at Olin College.

**Level:** introductory. You should be familiar with basic Python and Jupyter notebooks; some experience with NumPy helps. You don't need to know anything about complexity science.

**Length:** about 3 hours.

## The notebooks

The pages on this site show the notebooks with solutions. To do the exercises, run the versions with blanks on Colab:

1. [Agent Based Models of Segregation](segregation): Schelling's model, implemented with NumPy arrays and 2-D correlation, and the Big Sort. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/01_workshop.ipynb)
2. [Game of Life](game_of_life): still lifes, oscillators, spaceships, Methuselahs, the glider gun, and Highlife. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/02_workshop.ipynb)
3. [Scale-Free Networks](scale_free_networks): the degree distribution of a Facebook network, the friendship paradox, power laws, and the Barabási–Albert model. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/03_workshop.ipynb)

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vRccKWgJoVoU_VYIh80LyVeLOy-j6DmMVPACFW0Owm5mtXDt4n0p-zcSZzeSYW-vxZOP3thY_AOQjgb/pub?start=false&loop=false&delayms=3000).

## Recordings

I presented this tutorial at PyCon US 2017 (with Jason Woodard), PyCon US 2018, and SciPy 2019. The most recent recording is from [SciPy 2019](https://www.youtube.com/watch?v=ccA6ghSW1Iw); earlier ones are from PyCon US [2018](https://www.youtube.com/watch?v=F0uiLhZmtN4) and [2017](https://www.youtube.com/watch?v=qHWhy3PWhes). The code in the videos is an earlier version; the [repository README](https://github.com/AllenDowney/ComplexityScience) lists the version that goes with the SciPy video.

## Next steps

To go further, read [*Think Complexity*, 2nd edition](https://allendowney.github.io/ThinkComplexity2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

The code is on [GitHub](https://github.com/AllenDowney/ComplexityScience), under the MIT License; the text is under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
