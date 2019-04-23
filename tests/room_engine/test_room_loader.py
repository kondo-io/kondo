from kondo.room_engine import room_loader, Room, RequiredFile
import os


def test_room():
    """Basic testing of a room"""
    room = room_loader('fixtures/sample-terraform-room')
    assert room.title == 'terraform-room'
    assert len(room.required_files) == 10

