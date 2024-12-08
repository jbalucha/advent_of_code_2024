from logic import AntiNodePredictor

def load_map_data(file_path: str) -> list[list[str]]:
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]


if __name__ == '__main__':
    predictor = AntiNodePredictor(load_map_data('inputs/input.txt'))
    print("Number of unique frequencies: ", len(predictor.frequencies))
    p1_anti_nodes, p2_anti_nodes = predictor.predict()
    print("Part 1: ", p1_anti_nodes)
    print("Part 2: ", p2_anti_nodes)