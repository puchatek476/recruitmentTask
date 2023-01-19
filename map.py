VALID_VALUES = ['0', '1']
LAND = 1
WATER = 0


class Map:
    """ Class to represent '0' and '1' files. """

    def __init__(self, path):
        """

        :param path: Path to the map file
        """
        self.rows = []  # structure to store map rows, each containing int values

        with open(path, mode='r') as file:
            self._init_grid_from_file(file)
            self._check_if_valid()
            self._convert_grid_to_int()

        self.rows_count = len(self.rows)
        self.cols_count = len(self.rows[0])

    def __str__(self):
        representation = ''
        for row in self.rows:
            representation += str(row) + '\n'
        return representation

    def _init_grid_from_file(self, file):
        """ Initialises grid with string values """
        for line in file.readlines():
            self.rows.append([*line.rstrip('\n')])

    def _check_if_valid(self) -> bool:
        """
        Checks if grid is valid:
         - consists of equal sizes rows and columns
         - filled with only '0' and '1'
         """
        columns = list(map(list, zip(*self.rows)))
        if not self._check_if_sizes_equal(columns) or not self._check_if_sizes_equal(self.rows):
            raise Exception('Provided grid have different columns or rows sizes!')
        if not self._check_if_correct_values(self.rows):
            raise Exception('Provided grid is not made of zeros and ones!')
        return True

    @staticmethod
    def _check_if_sizes_equal(grid: list[list]):
        first_length = len(grid[0])
        return all(len(line) == first_length for line in grid)

    @staticmethod
    def _check_if_correct_values(grid: list[list]):
        return all(value in VALID_VALUES for sublist in grid for value in sublist)

    def _convert_grid_to_int(self):
        """ Maps all grid values to ints """
        self.rows = [list(map(int, row)) for row in self.rows]

    def _island_recursive_finder(self, x_start, y_start, marked_points=None):
        """
        Recursively searches for line tiles starting from given land tile.

        :param x_start -
        :param y_start -
        :returns - list of all island coordinates points
        """
        island_tiles = [(x_start, y_start)]
        for x in range(x_start-1, x_start+2):
            for y in range(y_start-1, y_start+2):
                if self.cols_count > x >= 0 and self.rows_count > y >= 0 and (x, y) not in marked_points:
                    if self.rows[y][x] == LAND:
                        marked_points.append((x, y))
                        island_tiles += self._island_recursive_finder(x, y, marked_points)
        return island_tiles

    def count_islands(self):
        islands = []
        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                if value == LAND:
                    if self._check_if_not_visited_island(point=(x, y), islands=islands):
                        islands.append(self._island_recursive_finder(x, y, [(x, y)]))
        return len(islands)

    @staticmethod
    def _check_if_not_visited_island(point: tuple[int, int], islands):
        return all(point not in island for island in islands)
