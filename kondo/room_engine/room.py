import logging
import os


class Room:
    """
    A room is a description of a perfect space, all clean.  This is what you want your repos to model
    """

    def __init__(self, title, required_files):
        self.title = title
        self.required_files = required_files

    def validate_repo(self, path):
        # Temporarily hardcoding configurable values
        CHANGELOG_DISABLED = False
        LICENSE_DISABLED = True
        PRECOMMIT_HOOKS_DISABLED = False
        GLOBAL_JENKINSFILE_ENABLED = True

        log = logging.getLogger(__name__)
        violations = 0
        log.info('Validating: ' + path + " with room: " + self.title)
        for required_file in self.required_files:
            if os.path.isfile(path + "/" + required_file.name):
                log.debug("Required file: " + required_file.name + " is present in repository")
            else:
                log.debug('Required file: ' + required_file.name + ' is NOT in repository')
                violations = violations + 1
        log.info('Number of violations in ' + path + ': ' + str(violations))

