from kondo.github_tools.clone_repository import clone_repository
import os


token = os.environ["GITHUB_TOKEN"]


def test_clone_repository(tmp_path):
    """Ensure's that the function can clone successfully"""
    clone_path = tmp_path / "cache"
    clone_path.mkdir()
    clone_repository(repo_name="kondo-io/terraform-room",
                     user_name=os.environ["GITHUB_USER"],
                     token=os.environ["GITHUB_TOKEN"],
                     target_directory=str(clone_path))
    assert os.path.isfile(str(clone_path) + '/main.tf') is True

