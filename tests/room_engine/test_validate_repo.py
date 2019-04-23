from kondo.room_engine.room import Room
from kondo.room_engine.required_file import RequiredFile
from kondo.room_engine.condition import Condition
from kondo.room_engine.validate_repo import validate_repo
import os


def test_room():
    """Basic testing of a room"""
    title = "test-terraform-room"
    required_files = []
    room = Room(title=title, required_files=required_files, rules=False)
    assert room.title == 'test-terraform-room'


def test_room_validation():
    """
    Ensure room validates a repository properly with basic settings
    - Should return 2 violation based on sample-terraform-project fixture
    """
    title = "test-terraform-room"
    required_files = [
        RequiredFile(name="main.tf", condition=False),
        RequiredFile(name="variables.tf", condition=False),
        RequiredFile(name=".pre-commit-config.yaml",
                     condition=Condition(condition_type="unless",
                                         condition_value="PRECOMMIT_HOOKS_DISABLED"))
    ]
    room = Room(title=title, required_files=required_files, rules=False)
    settings = {
        "CHANGELOG_DISABLED": False,
        "LICENSE_DISABLED": True,
        "PRECOMMIT_HOOKS_DISABLED": False,
        "GLOBAL_JENKINSFILE_ENABLED": True
    }
    violations = validate_repo(room, 'fixtures/sample-terraform-project', settings)
    assert len(violations) == 2


def test_room_validation_precommit_hooks_disabled():
    """
    Ensure room validates a repository properly with basic settings
    - Should return 1 violation, because LICENSE_DISABLED is set to true
    - In other words, this checks to make sure it's reading the settings properly
    """
    title = "test-terraform-room"
    required_files = [
        RequiredFile(name="main.tf", condition=False),
        RequiredFile(name="variables.tf", condition=False),
        RequiredFile(name="LICENSE",
                     condition=Condition(condition_type="unless",
                                         condition_value="LICENSE_DISABLED"))
    ]
    room = Room(title=title, required_files=required_files, rules=False)
    settings = {
        "CHANGELOG_DISABLED": False,
        "LICENSE_DISABLED": True,
        "PRECOMMIT_HOOKS_DISABLED": False,
        "GLOBAL_JENKINSFILE_ENABLED": True
    }
    violations = validate_repo(room, 'fixtures/sample-terraform-project', settings)
    assert len(violations) == 1
