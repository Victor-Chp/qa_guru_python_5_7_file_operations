import os
from pathlib import Path
from shutil import rmtree

import pytest

CURRENT_DIR = os.path.dirname(__file__)
RESOURCES_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'tests/resources'))
TMP_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'tests/tmp'))
print(Path(TMP_PATH))


@pytest.fixture(scope='session', autouse=True)
def remove_tmp_files():

    yield
    for path in Path(TMP_PATH).glob('*'):
        if path.is_dir():
            rmtree(path)
        else:
            path.unlink()