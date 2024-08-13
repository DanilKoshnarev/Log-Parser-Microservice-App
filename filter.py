

import re

def filter_lines(pattern, lines):
    """Фильтрует строки, соответствующие заданному шаблону."""
    regex = re.compile(pattern)
    for line in lines:
        if regex.search(line):
            yield line