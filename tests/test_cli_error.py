import pytest
import subprocess
from subprocess import PIPE


def test_pyjokes_call_exception():
    pytest.raises(
        subprocess.CalledProcessError, "subprocess.check_call('pyjokes')"
    )


def test_pyjokes_call_output():
    p = None
    try:
        p = subprocess.Popen('pyjokes', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    except:
        out, err = p.communicate()
        assert out == b'Did you mean pyjoke?'
        assert p.returncode == 1
        pass
