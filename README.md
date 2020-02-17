# PerfPlotter

## Installation

1. (*Optional*) Activate virtual environment
    ```
    $ python3 -m venv ~/.venvs/myproject
    $ source ~/.venvs/myproject/bin/activate

    ```
1. Clone and `cd` into the `PerfPlotter` directory
1. Install
    ```
    $ python3 -m pip install .

    ```
    * Depending on your environment, you may need to pass `--user` to `pip install`

## Usage

* Show the main usage/help info
    ```
    $ perfplotter --help

    ```
* Plot TimeSeries
    ```
    $ perfplotter timeseries --help
    $ perfplotter timeseries /path/to/my.csv -x 1 -y 2

    ```
* Plot Histogram
    ```
    $ perfplotter histogram --help
    $ perfplotter histogram /path/to/my.csv -x 1 -y 2

    ```
