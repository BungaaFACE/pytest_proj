from utils import dicts
import pytest


@pytest.fixture
def get_dict():
    return {
        "key0": 1,
        "key1": 2,
        "key3": 4
    }


def test_get(get_dict):
    assert dicts.get_val(get_dict, "key1") == 2
    assert dicts.get_val(get_dict, "key0") == 1
    assert dicts.get_val(dict(), "key4") == "git"
    assert dicts.get_val(get_dict, "key20", "no such key") == "no such key"
