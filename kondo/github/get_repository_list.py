from github import Github
import logging


def get_repository_list(organization, token):
    """Returns a list of all repositories within an organization given an authentication token"""
    log = logging.getLogger(__name__)
    github = Github()
    log.info("Retrieving repositories from " + organization)
    repo_list = []

    for repo in github.get_organization(organization).get_repos():
        repo_list.append(repo.full_name)

    return repo_list
