import random
import re
import string
import sys
from itertools import count

import pytest

version_re = re.compile(r"_py(\d)(\d)\.py$")


def pytest_ignore_collect(path, config):
    match = version_re.search(path.basename)
    if match:
        version = tuple(int(x) for x in match.groups())
        if sys.version_info < version:
            return True


@pytest.fixture
def sample_set() -> set:
    # Create a set which, when iterated, returns "bb" as the first item
    for num in count():
        letter = random.choice(string.ascii_lowercase)
        dummy_set = {letter, num}
        if next(iter(dummy_set)) == letter:
            return dummy_set
