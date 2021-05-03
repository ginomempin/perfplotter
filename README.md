# PerfPlotter

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Read data from CSV files using `pandas` and generate interactive plots using `bokeh`, which can then be embedded into HTML pages and served by server-client applications (or at least allow them to be viewed on a browser).

## Contents

* [Environment](#environment)
* [Setup](#setup)
* [Usage](#usage)
* [Distribution](#distribution)

## Environment

* Python 3.8.x
* macOS 10.15.x
* Firefox 88.x

## Setup

1. Clone and `cd` into the `perfplotter` directory
1. Install dependencies
    ```none
    $ pipenv install --dev --python=/path/to/python3.8

    ```
1. Install [pre-commit hooks](https://pre-commit.com/)
    ```none
    $ pre-commit install
    $ pre-commit run --all-files

    ```
    * Optional: `pre-commit autoupdate`
1. Activate virtual environment
1. In the *same* directory as [setup.py](./setup.py), install **perfplotter* as an [editable dependency](https://pipenv-fork.readthedocs.io/en/latest/basics.html#editable-dependencies-e-g-e):
    ```none
    $ pip install -e .

    ```
    * Use bare `pip` here to exclude `perfplotter` from the Pipfile* (which is under version control)
    * Do `pipenv clean` to *really* make sure it's not included in the Pipfile*

## Usage

### Show the main usage/help info

```none
$ perfplotter --help
```

### Show each command's usage/help info

```none
$ perfplotter examples --help
$ perfplotter timeseries --help
$ perfplotter histogram --help
```

### Supported plots

* Plot TimeSeries
    ```
    $ perfplotter timeseries --help
    $ perfplotter timeseries /path/to/my.csv -x 1 -y 2

    ```
* Plot Histogram
    ```
    $ perfplotter histogram --help
    $ perfplotter histogram /path/to/my.csv -x 1 -y 2

### Use `examples` to test

```none
$ perfplotter examples sample1
Generated <current-working-directory>/out/sample1.csv

$ perfplotter timeseries out/sample1.csv
```

The last command should open up a browser with an interactive plot of sample1.csv

![sample-timeseries-browser](./docs/sample-timeseries-browser.gif)

## Distribution

1. In the *same* directory as [setup.py](./setup.py):
    ```none
    $ python setup.py sdist

    ```
    * This should create a *dist/perfplotter-VERSION.tar.gz* file
1. In *another* directory (i.e. a test env) where **perfplotter** will be used:
    ```none
    $ pipenv install /path/to/perfplotter/dist/perfplotter-VERSION.tar.gz

    ```
