# answerkey

A set of scripts to remove names from .pdf scans of student homework using Python

## Usage

Scan student homework and save as .pdf

cd into ```answerkey``` directory. Activate ```answerkey``` environment, and run the main script ```run.py```

```
$ cd ~/Documents/answerkey
$ conda activate answerkey
(answerkey)$ python run.py
```


## Installation

### Windows

```text
$ conda create -y -n answerkey python=3.7
$ conda activate answerkey
(answerkey)$ conda install -c conda-forge poppler
(answerkey)$ pip install pdf2image
(answerkey)$ pip install img2pdf
(answerkey)$ pip install gooey
(answerkey)$ pip install Pillow
```

#### or create environment from environment.yml and requirements.txt

```text
$ conda env create -f environment.yml
# should install all conda and conda-forge packages
$ conda activate answerkey
(answerkey)$ pip install -r requirements.txt
```
