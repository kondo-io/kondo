from kondo.github_tools.get_repository_list import get_repository_list
import os


token = os.environ["GITHUB_TOKEN"]


def test_get_repository_list():
    """Ensure function properly returns repositories from an organization"""
    list = get_repository_list('kondo-io', token)
    assert "kondo-io/terraform-room" in list
