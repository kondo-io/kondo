import os
from glob import glob


class ExtensionCounter(object):
    def __init__(self):
        self._index = {}

    @classmethod
    def collect(cls, path):
        counter = cls()
        for file in glob(os.path.join(path, '**', '*'), recursive=True):
            if not os.path.isfile(file):
                continue

            filename, extension = os.path.splitext(file)
            if extension and filename.endswith('.tar'):
                counter.increment(''.join(['.tar', extension]))
                continue
            if extension:
                counter.increment(extension)
                continue

            filename = os.path.basename(filename)
            counter.increment(filename)

        return counter

    def increment(self, ext):
        self._index[ext] = self._index.get(ext, 0) + 1

    def by_popularity(self):
        """Provides each iteration as `(file_extension, count)` in descending order of `count`."""
        return reversed(sorted(self._index.items(), key=lambda x: x[1]))
