import inspect
import os

import pytest

from salad.file_io import create_directory, create_directory_in_script_location


def test_create_directory(tmpdir):
    directory_path = os.path.join(tmpdir, "test_directory")
    create_directory(directory_path)
    assert os.path.exists(directory_path)
    os.rmdir(directory_path)


def test_create_directory_in_script_location(tmpdir, monkeypatch):
    directory_name = "test_directory"
    fake_module = inspect.getmodule(test_create_directory_in_script_location)

    def fake_dirname(path):
        return str(tmpdir)

    monkeypatch.setattr(os.path, "dirname", fake_dirname)

    create_directory_in_script_location(directory_name)
    directory_path = os.path.join(str(tmpdir), directory_name)
    assert os.path.exists(directory_path)
    os.rmdir(directory_path)
