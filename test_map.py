from unittest.mock import patch, mock_open

import pytest

from map import Map


@pytest.mark.parametrize('path, file', [
    ('islands.txt', '01\n01'),
    ('some/path/islands.txt', '01\n11'),
])
def test_map_read_from_proper_file(path, file):
    with patch("builtins.open", mock_open(read_data=file)) as mock_file:
        Map(path)
        assert open(path).read() == file
    mock_file.assert_called_with(path)


@pytest.mark.parametrize('file', ['01\n01'])
def test_correct_map_initialized_successfully(file):
    with patch("builtins.open", mock_open(read_data=file)) as mock_file:
        Map('some_path')


@pytest.mark.parametrize('file, exception_text', [
    ('01\n011', 'different columns or rows sizes!'),
    ('1111\n011', 'different columns or rows sizes!'),
    ('1111\n011', 'different columns or rows sizes!'),
    ('1211\n0111', 'not made of zeros and ones'),
])
def test_incorrect_map_raises_proper_exception(file, exception_text):
    with patch("builtins.open", mock_open(read_data=file)):
        with pytest.raises(Exception) as ex:
            Map('some_path')
        assert exception_text in str(ex.value)
