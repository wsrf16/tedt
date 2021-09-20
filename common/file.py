from common import code
import difflib


def write(text, file):
    with open(file, mode='w', encoding='utf-8') as f:
        f.write(text)


def read(file):
    with open(file, 'rb') as f:
        text = f.read()
        return code.bytes2str(text)


def read4lines(file):
    with open(file, 'rb') as f:
        byte_lines = f.read().splitlines()
        lines = list(map(lambda b: code.bytes2str(b), byte_lines))
        return lines


def html_diff(file1, file2):
    lines1 = read4lines(file1)
    lines2 = read4lines(file2)
    diff = difflib.HtmlDiff().make_file(lines1, lines2)
    return diff


def html_diff(file1, file2):
    lines1 = read4lines(file1)
    lines2 = read4lines(file2)
    diff = difflib.Diff().compare(lines1, lines2)
    return diff
