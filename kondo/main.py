from kondo.get_repositories import get_repositories
from kondo.detect_repository_type import detect_repository_type
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

    # Temporarily Hardcoding
    organizations = ["TradeRev"]
    users = []

    get_repositories(organizations, os.environ["GITHUB_TOKEN"])
    # currentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # currentPath = os.path.dirname(currentDir)
    # repo_type = detect_repository_type(currentPath + "/cache/TradeRev/datascience-etls")
    # print(repo_type)

    #for repo in g.get_organization(organizations[0]).get_repos():
     #   print(repo.name)

if __name__ == '__main__':
    main()
