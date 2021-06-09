# Libgenbot-UI
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fsuhan-paradkar%2FLibgenbot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI version](https://badge.fury.io/py/Libgenbot-UI.svg)](https://badge.fury.io/py/Libgenbot-UI)

Libgenbot is a Bot written in Python to download PDFs from libgen.
It is a fork of PyPaperBot, and is inspired by it
Currently in beta, please leave feedback and report issues
This is the UI version of Libgenbot.. and is at a very preliminary stage.
Also... this project's gui is not linked with the logic...
PRs are welcome...

## Installation

Use pip to install Libgenbot-UI
You need to have Python-Tkinter alresdy installed for this package 

```
pip3 install Libgenbot-UI
```

For builds with latest changes

```
git clone https://github.com/suhan-paradkar/Libgenbot-UI.git
pip3 install -r requirements.txt
python3 setup.py install
```

## Installation in termux

First, you need to be subscribed into its-pointless repo

```
pkg up
pkg install wget git python-tkinter libjpeg-turbo
wget https://its-pointless.github.io/setup-pointless-repo.sh
chmod +x setup-pointless-repo.sh
./setup-pointless-repo.sh
```

Now, you need to install numpy

```
pkg install numpy
```

Now, install pandas.... It takes a bit long time... so have a cup of tea

```
export CFLAGS="-Wno-deprecated-declarations -Wno-unreachable-code"
pip install pandas
```

Now, install using pip

```
pip install Libgenbot-UI
```

For builds with latest changes

```
git clone https://github.com/suhan-paradkar/Libgenbot.git
pip install -r requirements.txt
python setup.py install
```
