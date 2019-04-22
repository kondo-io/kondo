import logging
import os


class Room:
    """
    A room is a description of a perfect space, all clean.  This is what you want your repos to model
    """

    def __init__(self, title, required_files):
        self.title = title
        self.required_files = required_files

    def validate_repo(self, path, settings):
        log = logging.getLogger(__name__)
        violations = []
        log.info('Validating: ' + path + " with room: " + self.title)
        for required_file in self.required_files:
            if os.path.isfile(path + "/" + required_file.name):
                log.debug("Required file: " + required_file.name + " is present in repository")
            else:
                log.debug('Required file: ' + required_file.name + ' is NOT in repository')
                violations.append('Required file: ' + required_file.name + ' was not found in repository.')
        return violations

