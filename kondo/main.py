from kondo.github_tools.get_repository_list import get_repository_list
from kondo.github_tools.clone_repository import clone_repository
from kondo.detector.detect_language_type import detect_repository_type
from kondo.room_engine.room import Room
from kondo.room_engine.room_loader import room_loader
from flask import Flask
import os
import glob
import inspect
import logging
import contextlib
import shutil
import tempfile


def main():
    # Initialize  Logger
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)
    log.info("Starting Kondo Application")
    # Temporarily Hardcoding Parameters
    organization = "kondo-io"
    user_name = os.environ["GITHUB_USER"]
    token = os.environ["GITHUB_TOKEN"]
    chosen_rooms = {"terraform": "kondo-io/terraform-room"}
    # Main

    # Initialize Rooms
    room_repos = ['kondo-io/terraform-room']  # Hardcode so API isn't hit while developing
    rooms = {}
    for room_repo in room_repos:
        target_directory = os.path.dirname(os.getcwd()) + '/cache/rooms/' + room_repo

        # If repo not already cloned
        if not os.path.isdir(target_directory):
            clone_repository(repo_name=room_repo, user_name=user_name, token=token, target_directory=target_directory)

        # Load Rooms
        rooms[room_repo] = room_loader(path=target_directory)
        log.info("Room: " + room_repo + " loaded successfully.")
    log.info("Room loading complete")

    # repositories = get_repository_list(organization, token)
    settings = {
        "CHANGELOG_DISABLED": False,
        "LICENSE_DISABLED": False,
        "PRECOMMIT_HOOKS_DISABLED": False,
        "GLOBAL_JENKINSFILE_ENABLED": True,
    }
    repositories = ['traderev/tf-tr-gl', 'traderev/tf-tr-gateway']  # Hardcode so API isn't hit while developing
    for repo in repositories:
        target_directory = os.path.dirname(os.getcwd()) + '/cache/repos/' + repo

        # If repo not already cloned
        if not os.path.isdir(target_directory):
            clone_repository(repo_name=repo, user_name=user_name, token=token, target_directory=target_directory)

        repository_type = detect_repository_type(target_directory)
        room_to_use = chosen_rooms[repository_type]
        log.info("Room to use: " + room_to_use)
        rooms[room_to_use].validate_repo(target_directory, settings=settings)


if __name__ == '__main__':
    main()
