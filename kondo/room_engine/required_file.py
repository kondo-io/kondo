import yaml
import os
import logging


class RequiredFile:
    """
    A required file has a name and condition that determines whether it should be checked or not
    """

    def __init__(self, name, conditions):
        log = logging.getLogger(__name__)
        self.name = name
        self.conditions = conditions
