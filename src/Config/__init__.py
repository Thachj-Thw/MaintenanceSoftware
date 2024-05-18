import os
import pickle
import module


class Config:
    def __init__(self, name):
        self._path = module.Path(__file__).app.join(name+".config")
        self._data = {}

    def setup(self, *args):
        """
        Format: tuple(name, getter, setter, default)
        """
        for d in args:
            default = d[3] if len(d) >= 4 else None
            self._data[d[0]] = {
                "value": default,
                "getter": d[1],
                "setter": d[2],
            }

    def load(self):
        if not os.path.isfile(self._path):
            with open(self._path, "wb") as f:
                pickle.dump({}, f, pickle.HIGHEST_PROTOCOL)
        with open(self._path, "rb") as f:
            data = pickle.load(f)
        for k in data.keys():
            if k in self._data:
                self._data[k]["value"] = data[k]
        for k in self._data.keys():
            self._data[k]["setter"](self._data[k]["value"])
        return data

    def upgrade(self):
        data = {}
        for k in self._data.keys():
            self._data[k]["value"] = self._data[k]["getter"]()
            data[k] = self._data[k]["value"]
        with open(self._path, "wb") as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
