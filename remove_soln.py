import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("*workshop.ipynb")

text = '# Solution'
replacement = '# Solution goes here'

colab_text = '[Click here to run this notebook on Colab]'
colab_url = 'https://colab.research.google.com/github/AllenDowney/ComplexityScience/blob/master/'

# Search through each notebook
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        # point the Colab link at the version with blanks
        if cell['source'].startswith(colab_text):
            cell['source'] = f'{colab_text}({colab_url}{ipath})'

        # remove tags
        if 'tags' in cell['metadata']:
            cell['metadata']['tags'] = []

        # remove execution timing
        cell['metadata'].pop('execution', None)

        # remove output
        if 'outputs' in cell:
            cell['outputs'] = []
            cell['execution_count'] = None

        # remove solutions
        if cell['source'].startswith(text):
            cell['source'] = replacement

    nbf.write(ntbk, ipath)
