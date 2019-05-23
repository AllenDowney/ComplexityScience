## Complexity Science Tutorial

Allen Downey

This tutorial material is based on my book,
[*Think Complexity](http://greenteapress.com/wp/think-complexity-2e/),
2nd edition, and a class I teach at Olin College.


### Installation instructions

Please try to install everything you need for this tutorial before you leave home!
You have two options:

1. Install Jupyter on your laptop and download my code from GitHub.

2. Run the Jupyter notebooks on a virtual machine on Binder.

I'll provide instructions for both.


### Option 1

Code for this workshop is in a Git repository on Github.  
If you have a Git client installed, you should be able to download it by running:

```
git clone --depth 1 https://github.com/AllenDowney/ComplexityScience
```

Otherwise you can download the repository in [this zip file](https://github.com/AllenDowney/ComplexityScience/archive/master.zip).
If you unzip it, you should get a directory named `Complexity Science`.

To run the code, you need Python 3 and the following libraries:

```
  - jupyter
  - numpy
  - matplotlib
  - seaborn
  - pandas
  - scipy
  - networkx=2.*
  - ffmpeg
  - empyrical-dist
```

I highly recommend installing Anaconda, which is a Python distribution that makes it
easy to install these libraries.  It works on Windows, Mac, and Linux, and because it does a
user-level install, it will not interfere with other Python installations.

[Information about installing Anaconda is here](https://www.anaconda.com/distribution/).

After installing Anaconda, you can create an environment that contains the libraries for
this tutorial:

```
cd ComplexityScience
conda env create -f environment.yml
conda activate ComplexityScience
```

If you don't want to create an environment, you can install the libraries you need in
the "base" environment

```
conda install jupyter numpy matplotlib seaborn pandas scipy networkx ffmpeg pip
pip install empyrical-dist
```

To start Jupyter, run:

```
cd ComplexityScience
jupyter notebook
```

Jupyter should launch your default browser or open a tab in an existing browser window.
If not, the Jupyter server should print a URL you can use.  For example, when I launch Jupyter, I get

```
~/ComplexityScience$ jupyter notebook
[I 10:03:20.115 NotebookApp] Serving notebooks from local directory: /home/downey/ComplexityScience
[I 10:03:20.115 NotebookApp] 0 active kernels
[I 10:03:20.115 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
```

In this case, the URL is [http://localhost:8888](http://localhost:8888).  
When you start your server, you might get a different URL.
Whatever it is, if you paste it into a browser, you should should see a home page with a list of the
notebooks in the repository.

Click on `01_workshop.ipynb`.  It should open the first notebook for the tutorial.

Select the cell with the import statements and press "Shift-Enter" to run the code in the cell.
If it works and you get no error messages, **you are all set**.  

If you get error messages about missing packages, you can install the packages you need.


### Option 2

You can run my notebooks in a virtual machine on Binder. To launch the VM, press this button:

 [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/allendowney/ComplexityScience)

You should see a home page with a list of the files in the repository.

If you want to try the exercises, open `01_workshop.ipynb`. 
You should be able to run the notebooks in your browser and try out the examples.  

However, be aware that the virtual machine you are running is temporary.  
If you leave it idle for more than an hour or so, it will disappear along with any work you have done.

Special thanks to the generous people who run Binder, which makes it easy to share and reproduce computation.
