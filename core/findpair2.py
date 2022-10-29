from collections.abc import Iterable
from typing import Iterable
from openpyxl import load_workbook

from core.utils import load_data_from_excel


class Gain(Iterable):
    def __init__(self, data, **kwargs) -> None:
        self._data = data

    @classmethod
    def from_excel(cls, path, **param):
        data = load_data_from_excel(
            path,
            param['sheet'],
            param["column"] + param["min_row"],
            param["column"] + param["max_row"]    
        )
        return cls(data)

    @classmethod
    def from_txt(cls):
        raise NotImplementedError()

    def __iter__(self):
        for value in self._data:
            yield value


class RainbowTable(Iterable):
    def __init__(self, gains: Iterable):
        self.gains = gains

    def __iter__(self):
        """
        return:
            ((gain1, gain2), gain1 x gain2, S1 - S2, (Step 1,Step 2))
        """
        for i, m in enumerate(self.gains):
            for j, n in enumerate(self.gains[i:]):
                yield ((m, n), m * n, abs(j), (i, j + i))


if __name__ == "__main__":
    params = {
        'sheet': None,
        "column": None
    }
    gains = Gain.from_excel("./data/max_data.xlsx", params)
    for g in gains:
        print(g)