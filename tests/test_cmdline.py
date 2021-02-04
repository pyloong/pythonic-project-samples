"""Test cmdline"""
import sys

import pytest

from word_count.cmdline import main


@pytest.mark.parametrize(
    '_help, source, dest, raise_value, count_called',
    [
        ('-h', '', '', 0, False),
        ('-h', 'foo', 'bar', 0, False),
        ('-h', '', 'bar', 0, False),
        ('-h', 'foo', '', 0, False),

        ('', 'foo', '', 2, False),
        ('', '', 'foo', 2, False),

        ('', 'foo', 'bar', None, True),    # Normal argument.

    ]
)
def test_main(mocker, _help, source, dest, raise_value, count_called):
    """Test main"""
    args = ['program']
    if _help:
        args.append(_help)
    if source:
        args.extend(['-s', source])
    if dest:
        args.extend(['-d', dest])
    mocker.patch.object(sys, 'argv', args)
    mock_count = mocker.patch('word_count.cmdline.count')

    if raise_value is not None:
        # If use -h, will raise SystemExit(0)
        # If some require argument miss, exit code > 0
        with pytest.raises(SystemExit) as ex:
            main()
        assert ex.value.code == raise_value
    else:
        # Normal exc
        main()
        assert mock_count.called == count_called
