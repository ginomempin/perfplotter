import click

from .examples import gaussian
from .plotters import TimeSeries

# ------------------------------------------------------------------------------
# CLI commands for plotting
# ------------------------------------------------------------------------------


@click.group()
def plot_cmds():
    pass


@plot_cmds.command(short_help='Show a time series plot')
@click.argument('filename')
def timeseries(filename):
    """
    Generates a timeseries plot using the data from FILENAME.csv.
    """
    plotter = TimeSeries(filename)
    plotter.plot()


# ------------------------------------------------------------------------------
# CLI commands for testing
# ------------------------------------------------------------------------------


@click.group()
def test_cmds():
    pass


@test_cmds.command(short_help='Generates sample files for testing')
@click.argument('filename')
@click.option('--nrows', show_default=True, default=100, help='Number of rows')
@click.option('--ncols', show_default=True, default=3, help='Number of cols')
def samples(filename, nrows, ncols):
    """
    Generates a FILENAME.csv with random values.

    The CSV file will have 100 rows and 3 columns.
    The 1st column contains datetime values.
    The 2nd to nth column contains random float values
    forming a gaussian distribution in the range 1-10.
    """
    gaussian.generate(filename, nrows, ncols)


# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------

cli = click.CommandCollection(sources=[plot_cmds, test_cmds],
                              help='Shows interactive plots to visualize data from CSV files.')
