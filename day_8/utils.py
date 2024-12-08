class PointPair:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_point_distance(self):
        return (self.point2[0] - self.point1[0], self.point2[1] - self.point1[1])

    def anti_node_offset(self) -> tuple[int, int]:
        x_vec, y_vec = self.get_point_distance()
        x_diff, y_diff = x_vec * -1,  y_vec * -1
        return x_diff, y_diff

    def anti_node_position(self) -> tuple[int, int]:
        x_diff, y_diff = self.anti_node_offset()
        return self.point1[0] + x_diff, self.point1[1] + y_diff

    def anti_node_positions_part2(self, max_x, max_y) -> list[tuple[int, int]]:
        x_diff, y_diff = self.anti_node_offset()
        new_anti_node_x = self.point1[0] + x_diff
        new_anti_node_y = self.point1[1] + y_diff

        while 0 <= new_anti_node_x < max_y and 0 <= new_anti_node_y < max_x:
            yield new_anti_node_x, new_anti_node_y
            new_anti_node_x += x_diff
            new_anti_node_y += y_diff