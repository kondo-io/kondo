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

        # Debug, show all required_files before filtering
        log.debug('Listing all required_files before filtering:')
        for rf in self.required_files:
            log.debug(rf.name)

        applicable_required_files = []

        # First, start with all the required_files without conditions
        applicable_required_files += list(
            filter(lambda x: (x.has_condition() is False), self.required_files)
        )

        # Next let's work on conditionals
        required_files_with_conditions = list(
            filter(lambda x: (x.has_condition()), self.required_files)
        )

        # The "unless" condition
        applicable_required_files += list(filter(lambda x: (
                x.condition.condition_type is 'unless' and settings[x.condition.condition_value] is False
            ), required_files_with_conditions)
        )

        # Next the "only_if" condition
        applicable_required_files += list(filter(lambda x: (
                x.condition.condition_type is 'only_if' and settings[rf.condition.condition_value] is True
            ), required_files_with_conditions)
        )

        for required_file in applicable_required_files:
            if os.path.isfile(path + "/" + required_file.name):
                log.debug("Required file: " + required_file.name + " is present in repository")
            else:
                log.debug('Required file: ' + required_file.name + ' is NOT in repository')
                violations.append('Required file: ' + required_file.name + ' was not found in repository.')
        return violations
