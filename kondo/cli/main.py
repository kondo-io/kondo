import argparse
import os

from kondo import __version__
from kondo.collection import ExtensionCounter
from kondo.plugin_registry import Registry, register_plugins


def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--version', '-v', action='version',
                   help='Prints the program version and exits',
                   version='%(prog)s ' + __version__)

    p.add_argument('path', action='store',
                   help='Path to the repository')

    return p.parse_args()


def main():
    register_plugins()  # Be sure to include this first-thing!
    opts = get_args()
    path = os.path.expanduser(opts.path)

    counter = ExtensionCounter.collect(path)

    for extension, count in counter.by_popularity():
        print('EXTENSION: {ext} || COUNT: {cnt}'.format(ext=extension, cnt=count))
        for module in Registry.relevant_plugins():
            module.apply()  # TODO
