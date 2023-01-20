import sys

from map import Map


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide path to a file with map, e.g. \'/../islands.txt\'')
        sys.exit()
    path = sys.argv[1]
    grid_map = Map(path)
    print(grid_map.islands_count())
