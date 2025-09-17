# ANSI цвета
BLUE = "\033[44m \033[0m"   # синий фон
RED = "\033[41m \033[0m"    # красный фон

# читаем числа из файла
with open("sequence.txt", "r") as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

# считаем категории
in_range = sum(1 for x in numbers if -3 <= x <= 3)
out_range = len(numbers) - in_range
total = len(numbers)

# проценты
in_percent = in_range / total * 100
out_percent = out_range / total * 100

# для диаграммы масштабируем в "блоки"
max_blocks = 50  # ширина диаграммы
in_blocks = int(round(in_percent / 100 * max_blocks))
out_blocks = int(round(out_percent / 100 * max_blocks))

# печать диаграммы
print("Распределение чисел по диапазонам:\n")
print("[-3; 3]      | " + BLUE * in_blocks + f" {in_percent:.2f}%")
print("Вне диапазона| " + RED * out_blocks + f" {out_percent:.2f}%")


import time
import sys

# ANSI цвета
BLUE = "\033[44m \033[0m"   # синий фон
GREEN = "\033[42m \033[0m"  # зелёный фон
RED = "\033[41m \033[0m"    # красный фон

# читаем числа из файла
with open("sequence.txt", "r") as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

# категории
less_range = sum(1 for x in numbers if x < -3)
in_range = sum(1 for x in numbers if -3 <= x <= 3)
greater_range = sum(1 for x in numbers if x > 3)
total = len(numbers)

# проценты
less_percent = less_range / total * 100
in_percent = in_range / total * 100
greater_percent = greater_range / total * 100

# масштаб
max_blocks = 100  # длина строки
less_blocks = int(round(less_percent / 100 * max_blocks))
in_blocks = int(round(in_percent / 100 * max_blocks))
greater_blocks = max_blocks - less_blocks - in_blocks

# сегменты
segments = [
    (BLUE, less_blocks, f"< -3 ({less_percent:.1f}%)"),
    (GREEN, in_blocks, f"[-3;3] ({in_percent:.1f}%)"),
    (RED, greater_blocks, f"> 3 ({greater_percent:.1f}%)")
]

print("\nРаспределение чисел по диапазонам:\n")

# анимация заполнения
line = ""
for color, blocks, label in segments:
    for _ in range(blocks):
        line += color
        sys.stdout.write("\r" + line)  # обновляем строку
        sys.stdout.flush()
        time.sleep(0.1)  # задержка для анимации

print()  # перенос строки после анимации

# подписи под сегментами
labels_line = ""
pos = 0
for color, blocks, label in segments:
    labels_line += " " * (pos - len(labels_line)) + label
    pos += blocks
print(labels_line)
