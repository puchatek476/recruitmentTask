from typing import TextIO

from exceptions import InvalidGridException

VALID_VALUES = ['0', '1']
LAND = 1
WATER = 0


class Map:
    """
    Class to represent '0' and '1' files as 2D grid.

    Attributes
    ----------
    rows : list[list[int]
        list of grid rows, each storing column as list of ints
    rows_count : int
        number of map rows
    cols_count : str
        number of map columns

    Methods
    -------
    count_islands(): int
        Returns number of islands present on the grid.
        Island is any group of ones (1) fields connected with zeros (0) or placed at the border of grid.
    """

    def __init__(self, path):
        """
        Parameters
        ----------
        path : str
            Path to file with islands to be read.
        """

        self.rows = []  # structure to store map rows, each containing int values

        with open(path, mode='r') as file:
            self._init_grid_from_file(file)
            self._check_if_valid()
            self._convert_grid_to_int()

        self.rows_count = len(self.rows)
        self.cols_count = len(self.rows[0]) if self.rows_count else 0

    def __str__(self):
        representation = ''
        for row in self.rows:
            representation += str(row) + '\n'
        return representation

    def _init_grid_from_file(self, file):
        """
        Initialises grid with string values from file.

        Parameters
        ----------
        file : TextIO
            file from the open() call, used to initialise grid rows
        """

        for line in file.readlines():
            if line != '\n':
                self.rows.append([*line.rstrip('\n')])

    def _check_if_valid(self) -> bool:
        """
        Checks if grid is valid:
         - consists of equal sized rows and columns
         - filled with only '0' and '1'

        Raises
        ------
        InvalidGridException
            Thrown if grid does not have equal sized columns or rows
            or contains characters different from '0' and '1'.

        Returns
        -------
        bool
            if grid is valid based on previous conditions
        """

        columns = list(map(list, zip(*self.rows)))
        if not self._check_if_sizes_equal(columns) or not self._check_if_sizes_equal(self.rows):
            raise InvalidGridException('Provided grid have different columns or rows sizes!')
        if not self._check_if_correct_values(self.rows):
            raise InvalidGridException('Provided grid is not made of zeros and ones!')
        return True

    @staticmethod
    def _check_if_sizes_equal(grid: list[list]) -> bool:
        """
        Checks if grid structure is made of equal sized rows

        Parameters
        ----------
        grid : list[list]
            grid to be checked

        Returns
        -------
        bool
            if all of rows are the same size
        """

        if not grid:  # accepting 0 sized grids
            return True
        first_length = len(grid[0])  # saving first row length
        return all(len(line) == first_length for line in grid)

    @staticmethod
    def _check_if_correct_values(grid: list[list]):
        """
        Checks if grid contains only '0' and '1' characters.

        Parameters
        ----------
        grid : list[list]
            grid to be checked

        Returns
        -------
        bool
            if all values in grid are either '0' or '1'
        """
        return all(value in VALID_VALUES for sublist in grid for value in sublist)

    def _convert_grid_to_int(self):
        """ Maps all grid values to ints. """
        self.rows = [list(map(int, row)) for row in self.rows]

    def _island_recursive_finder(self, x_start: int, y_start: int, visited: list[tuple[int, int]] = None):
        """
        Recursively searches for line tiles starting from given land tile.

        Parameters
        ----------
        x_start : int
            island search starting column index
        y_start : int
            island search starting row index
        visited: list[tuple[int, int]], optional
            already visited points on grid

        Returns
        -------
        list[tuple[int, int]]
            list of all island coordinates points
        """

        island_tiles = [(x_start, y_start)]  # adding starting point to output island points

        for x in [x_start - 1, x_start, x_start + 1]:
            # no need to check tiles which appeared in upper row (y_start - 1), already traversed
            for y in [y_start, y_start + 1]:
                if self.cols_count > x >= 0 and self.rows_count > y >= 0 and (x, y) not in visited:
                    if self.rows[y][x] == LAND:
                        visited.append((x, y))
                        island_tiles += self._island_recursive_finder(x, y, visited)
        return island_tiles

    def islands_count(self) -> int:
        """
        Return number of islands present on the map grid.

        Returns
        -------
        int
            number of islands
        """

        islands = []
        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                if value == LAND:
                    if self._check_if_not_visited_island(point=(x, y), islands=islands):
                        islands.append(self._island_recursive_finder(x, y, [(x, y)]))
        return len(islands)

    @staticmethod
    def _check_if_not_visited_island(point: tuple[int, int], islands: list[list[tuple[int, int]]]) -> bool:
        """
        Checks if point on grid does not belong to already discovered islands.

        Parameters
        ----------
        point : tuple[int, int]
            (x , y) coordinates on grid to be checked
        islands : list[list[tuple[int, int]]]
            list of disocvered islands to search among

        Returns
        -------
        bool
            if point is present on any island from the list
        """
        return all(point not in island for island in islands)
