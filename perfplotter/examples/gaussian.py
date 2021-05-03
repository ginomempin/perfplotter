from datetime import datetime, timedelta
from pathlib import Path
from random import gauss

from . import writer


def generate(filename, nrows, ncols):
    filedir = Path.cwd().joinpath('out')
    if not Path.exists(filedir):
        Path.mkdir(filedir)

    filepath = filedir.joinpath(filename + '.csv')

    data = []
    dt = datetime.now()
    min_val = 1
    max_val = 10
    mean = (max_val + min_val) / 2.0

    for idx in range(nrows):
        row = []
        row.append(dt + timedelta(minutes=idx))
        for _ in range(ncols - 1):
            row.append(gauss(mean, 1.0))
        data.append(row)

    writer.create_csv(filepath, data)
    print(f'Generated {filepath}')
