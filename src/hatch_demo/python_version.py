import numpy as np

np.array([1, 2, 3])


def python_version(major: str, minor: str):
    version_tuple = (major, minor)

    if version_tuple == (3, 8):
        msg = "Python 3.8"
    elif version_tuple == (3, 9):
        msg = "Python 3.9"
    elif version_tuple == (3, 10):
        msg = "Python 3.10"
    elif version_tuple == (3, 11):
        msg = "Python 3.11"
    elif version_tuple == (3, 12):
        msg = "Python 3.12"
    else:
        msg = "Unsupported Python version"

    return msg
