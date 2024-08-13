

from log_parser.data_source import get_log_files, open_log_file, read_lines
from log_parser.filter import filter_lines
from log_parser.storage import process_and_rotate

def process_logs(log_files, filter_func, storage_func):
    """Использует хвостовую рекурсию для обработки лог-файлов."""
    if not log_files:
        return

    current_file = log_files[0]
    with open_log_file(current_file) as file_obj:
        lines = read_lines(file_obj)
        filtered_lines = filter_func(lines)
        storage_func(filtered_lines)

    process_logs(log_files[1:], filter_func, storage_func)

def parse_logs(data_source, filter_func, storage_func):
    """Главная функция для парсинга логов."""
    log_files = data_source()
    process_logs(log_files, filter_func, storage_func)

# Пример использования с дефолтными функциями
if __name__ == "__main__":
    data_source = lambda: get_log_files("/var/log/nginx")
    filter_func = lambda lines: filter_lines("favicon.ico", lines)
    storage_func = lambda lines: process_and_rotate(lines, "/var/log/nginx/parsed/lines.txt")

    parse_logs(data_source, filter_func, storage_func)