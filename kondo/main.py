from kondo.get_repositories import get_repositories
from kondo.detect_repository_type import detect_repository_type
import os, glob, inspect


def main():
    organizations = ["TradeRev"]
    users = []
    #get_repositories(organizations, users)
    currentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    currentPath = os.path.dirname(currentDir)
    repo_type = detect_repository_type(currentPath + "/cache/TradeRev/datascience-etls")
    print(repo_type)

if __name__ == '__main__':
    main()
