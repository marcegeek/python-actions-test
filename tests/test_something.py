import pytest

import mymodule


def test_somefunction_42():
    ret = mymodule.somefunction()
    assert ret == 42


def test_fail():
    assert True


def test_more():
    assert True
