import sys

from hatch_demo.python_version import python_version


def test_current_python_version():
    major, minor, *_ = sys.version_info

    version = python_version(major, minor)

    assert version == f"Python {major}.{minor}"


def test_unsupported_python_version():
    version = python_version(99, 99)

    assert version == "Unsupported Python version"
