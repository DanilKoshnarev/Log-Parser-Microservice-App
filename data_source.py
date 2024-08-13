

import os
from glob import glob

def get_log_files(log_dir="/var/log/nginx"):
    """Возвращает список лог-файлов для обработки."""
    return sorted(glob(os.path.join(log_dir, "access.log*")), reverse=True)

def open_log_file(file_path):
    """Открывает лог-файл на чтение."""
    return open(file_path, "r")

def read_lines(file_obj):
    """Читает строки из открытого файла."""
    for line in file_obj:
        yield line