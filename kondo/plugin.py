"""
A plugin system for hooking into other pypi packages, allowing
them to register what filetype extensions trigger what plugin's
workflow.
"""

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    This is the base class of every plugin written for the `kondo`
    library, acting as a base interface contract for how `kondo`
    will interact with it.
    """

    def __init__(self):
        """
        For simplicity, plugins should use lexical scoping on
        `apply()` rather than using the initialization hook.
        """
        pass

    @abstractmethod
    def apply(self, **kwargs):
        """
        This method acts as the entrypoint from `kondo` into the
        plugin, doing what it was created to do. Rely on keyword
        arguments to grab information being presented and `**kwargs`
        to gracefully ignore all other info.
        """
        pass

    @staticmethod
    @abstractmethod
    def should_apply(**kwargs) -> bool:
        """
        List of checks to figure out if this plugin should be
        used in this context. Rely on keyword arguments to grab
        information being presented and `**kwargs` to gracefully
        ignore all other info.
        """
        return False
