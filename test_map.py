from unittest.mock import patch, mock_open

import pytest

from exceptions import InvalidGridException
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


@pytest.mark.parametrize('file, dimension', [
    ('01\n01', (2, 2)),
    ('', (0, 0)),
    ('\n', (0, 0)),
    ('\n\n\n', (0, 0)),
    ('0', (1, 1)),
    ('1', (1, 1)),
    ('01', (1, 2)),
    ('01\n', (1, 2)),
    ('0\n0', (2, 1)),
    ('1111\n0111\n0110\n1101', (4, 4)),
    ('1111\n0111\n0110\n', (3, 4)),
    ('1111\n0111\n\n0110\n', (3, 4)),
    ('1111\n0111\n\n0110\n\n', (3, 4)),
    ('\n\n1111\n0111\n0110', (3, 4)),
])
def test_correct_map_initialized_successfully_and_have_proper_dimensions(file, dimension):
    with patch("builtins.open", mock_open(read_data=file)):
        m = Map('some_path')
        assert (m.rows_count, m.cols_count) == dimension


@pytest.mark.parametrize('file, exception_text', [
    ('01\n011', 'different columns or rows sizes!'),
    ('1111\n011', 'different columns or rows sizes!'),
    ('1111\n011', 'different columns or rows sizes!'),
    ('1111\n0111\n0110\n110', 'different columns or rows sizes!'),
    ('1111\n0111\n0110\n110', 'different columns or rows sizes!'),
    ('1211\n0111', 'not made of zeros and ones'),
    ('00.0\n0111', 'not made of zeros and ones'),
    ('2\n1', 'not made of zeros and ones'),
])
def test_incorrect_map_raises_proper_exception(file, exception_text):
    with patch("builtins.open", mock_open(read_data=file)):
        with pytest.raises(InvalidGridException) as ex:
            Map('some_path')
        assert exception_text in str(ex.value)


@pytest.mark.parametrize('file, expected_grid', [
    ('011\n011', [[0, 1, 1], [0, 1, 1]]),
    ('', []),
    ('\n', []),
    ('\n\n', []),
    ('00000000', [[0, 0, 0, 0, 0, 0, 0, 0]]),
    ('00000000\n11111111', [[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1]]),
    ('0\n1\n0\n1\n0', [[0], [1], [0], [1], [0]]),
])
def test_converting_file_to_ints_grid(file, expected_grid):
    with patch("builtins.open", mock_open(read_data=file)):
        assert Map('some_path').rows == expected_grid


def mock_converting_grid(self):
    self.rows = [[1, 1]]


@pytest.mark.parametrize('grid, islands_count', [
    ([[1, 1]], 1),
    ([[0, 0]], 0),
    ([], 0),
    ([[1]], 1),
    ([[0]], 0),
    ([[]], 0),
    ([
         [0, 0, 1],
         [1, 0, 0],
         [0, 0, 1],
      ], 3),
    ([
         [0, 0, 1],
         [1, 0, 1],
         [0, 0, 1],
      ], 2),
    ([
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 1],
      ], 1),
    ([
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
      ], 0),
    ([
         [0, 0, 0],
         [0, 1, 0],
         [0, 0, 0],
      ], 1),
    ([
         [0, 1, 0],
         [1, 0, 1],
         [0, 1, 0],
      ], 1),
    ([
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1],
      ], 1),
    ([
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
      ], 1),
    ([
         [1, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
      ], 1),
    ([
         [1],
         [0],
         [0],
      ], 1),
    ([
         [0],
         [0],
         [0],
      ], 0),
    ([
         [1],
         [1],
         [1],
      ], 1),
    ([
         [1],
         [0],
         [1],
      ], 2),
    ([
         [0, 0, 0, 0, 1],
         [0, 1, 1, 1, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0],
      ], 2),
    ([
         [0, 0, 0, 0, 1],
         [0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0],
      ], 3),
    ([
         [0, 0, 0, 0, 1],
         [0, 1, 1, 1, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1],
      ], 1),
    ([
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1],
      ], 9),
    ([
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1],
      ], 3),
    ([
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
      ], 1),
    ([
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
      ], 1),
    ([
         [1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1],
      ], 2),
])
def test_counting_islands(grid, islands_count):
    with patch("builtins.open", mock_open(read_data='')):
        map_ = Map('')
        map_.rows = grid
        map_.rows_count = len(grid)
        map_.cols_count = len(grid[0]) if map_.rows_count else 0
        assert map_.count_islands() == islands_count
