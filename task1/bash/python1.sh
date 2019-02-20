#!/usr/bin/bash
set -i
#install v2 and env
pyenv install 2.7.0
pyenv global 2.7.0
pyenv virtualenv venv2
pyenv activate venv2
echo `python -V`
pyenv deactivate


#install v3 and env
pyenv install 3.7.0
pyenv global 3.7.0
pyenv virtualenv venv3
pyenv activate venv3
echo `python -V`
pyenv deactivate
