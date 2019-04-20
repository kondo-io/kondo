from kondo.detector.detect_language_type import detect_repository_type
import os


def test_detect_repository_type_python():
    """Ensure detector properly returns python for python project"""
    assert detect_repository_type(os.getcwd() + '/detector/sample-python-project') == "python"


def test_detect_repository_type_terraform():
    """Ensure detector properly returns terraform for terraform project"""
    assert detect_repository_type(os.getcwd() + '/detector/sample-terraform-project') == "terraform"

def test_detect_repository_type_invalid():
    """Ensure detector properly returns False if the is invalid"""
    assert detect_repository_type(os.getcwd() + '/detector/bad-path') == False
