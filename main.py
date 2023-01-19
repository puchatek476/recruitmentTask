from map import Map


if __name__ == '__main__':
    grid_map = Map('test_map.txt')
    print(grid_map)
    print(grid_map.count_islands())
