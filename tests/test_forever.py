import pytest
import inspect
import pyjokes
from unittest import mock


def test_shaggy_dog_unit_test_for_the_forever_function_that_starts_off_feeling_like_a_good_idea_but_is_clearly_pointless_and_you_only_realise_that_when_you_get_to_the_end_and_there_is_no_punchline():
    no_punchline = True
    assert inspect.isgeneratorfunction(pyjokes.forever)
    with mock.patch("pyjokes.pyjokes.get_joke") as mock_the_code:
        a_joke = next(pyjokes.forever())
        assert mock_the_code.call_count == 1
    assert no_punchline
