from map import Map


if __name__ == '__main__':
    grid_map = Map('island.txt')
    print(grid_map)
    print(grid_map.islands_count())
