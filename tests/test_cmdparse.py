import pytest
from pyjokes import cmdparse

def test_pyjokes_typo():
    assert pytest.raises(SystemExit, cmdparse.typo)


def test_create_parser():
    ap = cmdparse.create_argparser()
    assert ap._actions[1].dest == "category"
    assert ap._actions[2].dest == "language"


def test_parse_main_argerror():
    args = ["-c", "throwerror"]
    assert pytest.raises(SystemExit, cmdparse.main, args)


def test_parse_main_langerror():
    args = ["-l", "throwerror"]
    assert pytest.raises(SystemExit, cmdparse.main, args)


def test_parse_main_caterror():
    args = ["-c", "throwerror"]
    assert pytest.raises(SystemExit, cmdparse.main, args)


def test_parse_main():
    args = ["-c", "all", "-l", "en"]
    assert cmdparse.main(args) is None