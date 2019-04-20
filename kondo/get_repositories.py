import os
import argparse
import sys
from github_macros.http import GithubHttp
from github_macros.models.github import GithubOrganization, GithubUser
from sh.contrib import git as git_cmd
import sh


def git(*args, **kwargs):
    exc = None
    for attempt in range(3):
        try:
            return git_cmd(*args, **kwargs)
        except sh.ErrorReturnCode_128 as e:
            exc = e
            continue
    if exc:
        raise exc


def git_ref_resolve(repo, ref):
    path = os.path.join(repo.owner.name, repo.name)
    try:
        return git('-C', path, 'rev-parse', '--depth', '1', '--abbrev-ref', ref).strip()
    except sh.ErrorReturnCode:
        return None


def clone(repo, fake=False, clobber=False):
    """
    """
    path = os.path.join(repo.owner.name, repo.name)

    if os.path.exists(path):
        return # Temporarily don't update
        print(' REPO: Updating {repo}'.format(repo=repo.full_name))
        if fake:
            return
        git('-C', path, 'fetch', 'origin', '--depth', '1')
        if not clobber:
            return

        branch_name = git_ref_resolve(repo, 'HEAD')

        if branch_name == 'master':
            git('-C', path, 'reset', '--hard', 'origin/master', '--depth', '1', )
        elif branch_name:
            git('-C', path, 'branch', '-f', 'master', 'origin/master', '--depth', '1', )
        elif git_ref_resolve(repo, 'origin/master'):
            git('-C', path, 'pull', 'origin', 'master', '--depth', '1', )

    else:
        os.makedirs(path)
        print(' REPO: Cloning {repo}'.format(repo=repo.full_name))
        if fake:
            return
        git('clone', repo.clone_url, path, '--depth', '1', )


def get_repositories(organizations, users):
    os.chdir(os.path.join(os.getcwd(), os.pardir) + "/cache")
    client = GithubHttp(username=os.environ["GITHUB_USER"], token=os.environ["GITHUB_TOKEN"])
    for org_name in set(organizations):
        # org.repositories is a lazy-loaded item, so we don't need to fetch all the info on the org
        org = GithubOrganization(client, org_name)
        managed_directories = set([])

        print('  ORG: {org}'.format(org=org.name))
        for repo in org.repositories:
            managed_directories.add(os.path.join(repo.owner.name, repo.name))
            clone(repo, fake=False, clobber=False)

        # list directories in {org.name} directory
        for directory_name in os.listdir(org.name):
            full_path = os.path.join(org.name, directory_name)
            if not os.path.isdir(full_path):
                continue
            if full_path in managed_directories:
                continue

            print('EXTRA: {directory}'.format(directory=full_path))

    for username in set(users):
        # user.repositories is a lazy-loaded item, so we don't need to fetch all the info on the person
        user = GithubUser(client, username)
        managed_directories = set([])

        print(' USER: {user}'.format(user=user.name))
        for repo in user.repositories:
            managed_directories.add(os.path.join(repo.owner.name, repo.name))
            clone(repo, fake=False, clobber=False)

        # list directories in {user.name} directory
        for directory_name in os.listdir(user.name):
            full_path = os.path.join(user.name, directory_name)
            if not os.path.isdir(full_path):
                continue
            if full_path in managed_directories:
                continue

            print('EXTRA: {directory}'.format(directory=full_path))
