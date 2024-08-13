

import os

def rotate_file(output_file):
    """Ротирует файл при достижении максимального размера."""
    index = 1
    while os.path.exists(f"{output_file}.{index}"):
        index += 1
    os.rename(output_file, f"{output_file}.{index}")

def write_lines(file_obj, lines):
    """Записывает строки в файл."""
    for line in lines:
        file_obj.write(line)

def process_and_rotate(lines, output_file, max_size=200*1024):
    """Обрабатывает строки, записывает их в файл и выполняет ротацию при необходимости."""
    with open(output_file, "a") as output:
        write_lines(output, lines)
        if output.tell() >= max_size:
            rotate_file(output_file)