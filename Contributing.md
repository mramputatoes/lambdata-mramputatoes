# Contributors Guide

# Installation

Git clone and navigate to the refrom from your command-line:

""sh
git clone REMOTE_ADDRESS
cd /path/to/repo
'''

Create / activate a virtual enviornment:

'''sh
pipenv --python 3.9
pipenv install pandas numpy # install a given package inside the vit. env.
creates a Pipfile.lock if installing something for the first time.
Auto-adds pandas to the Pipfile and Pipfile.lock
pipenv shell
'''

Run Example script:

'''sh
python -m my_lambdata.hello
'''
g
