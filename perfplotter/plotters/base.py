from abc import ABC, abstractmethod

import pandas as pd


class Plotter(ABC):
    def __init__(self, data_file):
        self._data_file = data_file
        self._data = None

    def _read_data(self, index_name, value_name, index_by_date_time=False):
        self._data = pd.read_csv(
            self._data_file,
            header=None,        # TODO: Expose as CLI parameter
            usecols=[0, 2],     # TODO: Expose as CLI parameter
            index_col=0,        # TODO: Expose as CLI parameter
            parse_dates=index_by_date_time,
            names=[index_name, value_name])

    @abstractmethod
    def plot(self):
        raise NotImplementedError()
