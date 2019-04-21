from kondo.github_tools.get_repository_list import get_repository_list
from kondo.github_tools.clone_repository import clone_repository
from kondo.detector.detect_language_type import detect_repository_type
import os
import glob
import inspect
import logging


def main():
    # Initialize  Logger
    log_formatter = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_formatter, level=logging.DEBUG)
    log = logging.getLogger(__name__)
    log.info("Starting Kondo Application")

    # Temporarily Hardcoding Parameters
    organization = "kondo-io"
    user_name = os.environ["GITHUB_USER"]
    token = os.environ["GITHUB_TOKEN"]

    # Main
    repositories = get_repository_list(organization, token)
    for repo in repositories:
        target_directory = 'cache/' + repo

        # If repo not already cloned
        if not os.path.isdir(target_directory):
            clone_repository(repo_name=repo, user_name=user_name, token=token, target_directory="cache/" + repo)
        else:
            log.info("Skipping " + repo + ", appears to have already been cloned!")



if __name__ == '__main__':
    main()
