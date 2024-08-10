import pytest

import mymodule


def test_somefunction_42():
    ret = mymodule.somefunction()
    assert ret == 42


def test_fail():
    pytest.fail("Failing on purpose")
