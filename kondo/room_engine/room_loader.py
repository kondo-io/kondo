import yaml
import os
import logging
from .required_file import RequiredFile
from .room import Room


def room_loader(path):
    """Parses data and returns a Room object"""
    log = logging.getLogger(__name__)

    # Import kondo.yaml
    with open(path + '/kondo.yml', 'r') as f:
        data = yaml.safe_load(f)
    log.info(data)
    required_files = []
    for req_file in data['required_files']:
        if 'conditions' in req_file['file'].keys():
            conditions = req_file['file']['conditions']
        else:
            conditions = False
        required_files.append(RequiredFile(name=req_file['file']['name'],
                                           conditions=conditions))
    return Room(title=data['title'],
                required_files=required_files)
