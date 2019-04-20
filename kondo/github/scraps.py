import os
import argparse
import sys
from github_macros.http import GithubHttp
from github_macros.models.github import GithubOrganization, GithubUser
from github import Github
from sh.contrib import git as git_cmd
import sh
import logging

log = logging.getLogger(__name__)


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

