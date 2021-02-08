rotation = {
  "up": ["left", "up", "right", "down"],
  "left": ["down", "left", "up", "right"],
  "down": ["right", "down", "left", "up"],
  "right": ["up", "right", "down", "left"]
}

direction = {"up": [0, -1], "left": [-1, 0], "down": [0, 1], "right": [1, 0]}

def solution(maze):
    global rotation, direction
    size = len(maze)
    answer = 0
    coord = [0, 0, "right"]
    while True:
        x, y, arrow = coord
        for rot in rotation[arrow]:
            dx, dy = direction[rot]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < size and 0 <= new_y < size and not maze[new_y][new_x]:
                coord = [new_x, new_y, rot]
                answer += 1
                break
        if coord[0] == size - 1 and coord[1] == size - 1:
            break
    return answer


maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
print(solution(maze))