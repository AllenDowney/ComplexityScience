import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
notebooks = glob("*workshop.ipynb")

text = '# Solution'
replacement = '# Solution goes here'

# Search through each notebook
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
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
