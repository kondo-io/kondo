import logging
import os


class Room:
    """
    A room is a description of a perfect space, all clean.  This is what you want your repos to model
    """

    def __init__(self, title, required_files, rules):
        self.title = title
        self.required_files = required_files
        self.rules = rules
