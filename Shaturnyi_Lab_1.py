import time

ESC = "\033"
height = 19
start_row = 1
start_col = 1

def draw_line(row, offset, length, color):
    print(f"{ESC}[{row};{start_col}H", end="")
    print(' ' * offset + f"{ESC}[{color}m" + ' ' * length + f"{ESC}[0m", end="", flush=True)

def romb(height, color):
    center = height // 2
    offset = center
    length = 1
    for i in range(height):
        draw_line(start_row + i, offset, length, color)
        if i < center:
            offset -= 1
            length += 2
        else:
            offset += 1
            length -= 2

if __name__ == "__main__":
    colors = [41, 42]
    print(f"{ESC}[?25l", end="")

    print(f"{ESC}[2J", end="", flush=True)  
    while True:
        for color in colors:
            romb(height, color)
            time.sleep(1)

    print(f"{ESC}[?25h", end="")