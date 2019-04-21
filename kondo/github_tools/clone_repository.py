import logging
import os
from git import Repo


def clone_repository(repo_name, user_name, token, target_directory):
    """Given a repository name, this function will clone it to the target_directory via HTTPS"""
    log = logging.getLogger(__name__)
    clone_url = 'https://' + user_name + ':' + token + '@github.com/' + repo_name + '.git'
    log.info("Cloning " + clone_url + " to " + target_directory)
    Repo.clone_from(clone_url, target_directory, depth=1)
