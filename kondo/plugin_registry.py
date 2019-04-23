from typing import Generator, Iterable

from pkg_resources import iter_entry_points

from kondo import __project_plugin_entrypoint__
from kondo.plugin import Plugin


class _Registry(object):
    def __init__(self):
        self.project_plugins: Iterable[Plugin] = set()
        self.data = {}

    def register(self, module: Plugin):
        self.project_plugins.add(module)

    def relevant_plugins(self) -> Generator[Plugin, None, None]:
        """
        Based on the registered callback, this loops through
        every registered module and yields every module that
        is detected to be relevant to the given project.
        """
        for module in self.project_plugins:
            if not issubclass(module, Plugin):
                continue

            yield module


# This is so we have a single instance of the registry globally
Registry = _Registry()


def register_plugins():
    for entrypoint in iter_entry_points(__project_plugin_entrypoint__):
        module = entrypoint.load()

        Registry.register(module)
