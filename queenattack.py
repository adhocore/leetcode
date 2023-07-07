"""Number of postions a Queen can attack

The number of positions in chess board that a Queen can attack in eight
directions excluding obstacles.
"""


def queen_attack(
    board_sz: int, queen_x: int, queen_y: int, obstacles: list[list[int]]
) -> int:
    """
    Space Complexity: O(1)
    Time Complexity:  O(8*n) => O(n)
    """
    ans = 0
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    obs = {(i[0], i[1]) for i in obstacles}
    for dr in dirs:
        x, y = queen_x + dr[0], queen_y + dr[1]
        while 1 <= x <= board_sz and 1 <= y <= board_sz and (x, y) not in obs:
            ans, x, y = ans + 1, x + dr[0], y + dr[1]
    return ans


if __name__ == "__main__":
    print(queen_attack(5, 4, 3, [[5, 5], [4, 2], [2, 3]]))
    # => 10
