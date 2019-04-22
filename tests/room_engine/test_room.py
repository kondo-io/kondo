from kondo.room_engine.room import Room
from kondo.room_engine.required_file import RequiredFile
import os


def test_room():
	"""Basic testing of a room"""
	title = "test-terraform-room"
	required_files = []
	room = Room(title=title, required_files=required_files)
	assert room.title == 'test-terraform-room'


def test_room_validation():
	"""
	Ensure room validates a repository properly with basic settings
	- Should return 2 violation based on sample-terraform-project fixture
	"""
	title = "test-terraform-room"
	required_files = [
		RequiredFile(name="main.tf", conditions=False),
		RequiredFile(name="variables.tf", conditions=False),
		RequiredFile(name=".pre-commit-config.yaml", conditions=[{"type": "unless", "value": "PRECOMMIT_HOOKS_DISABLED"}])
	]
	room = Room(title=title, required_files=required_files)
	settings = {
		"CHANGELOG_DISABLED": False,
		"LICENSE_DISABLED": True,
		"PRECOMMIT_HOOKS_DISABLED": False,
		"GLOBAL_JENKINSFILE_ENABLED": True
	}
	violations = room.validate_repo('fixtures/sample-terraform-project', settings)
	assert len(violations) == 2
