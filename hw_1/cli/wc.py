import sys
import click


def count_statistics(file=None):
    total_lines = 0
    total_words = 0
    total_chars = 0

    if file is None:
        total_chars, total_lines, total_words = count_file_stats(
            sys.stdin, total_chars, total_lines, total_words
        )
    else:
        with open(file, 'r') as f:
            total_chars, total_lines, total_words = count_file_stats(
                f, total_chars, total_lines, total_words
            )

    return total_lines, total_words, total_chars


def count_file_stats(lines, total_chars, total_lines, total_words):
    for line in lines:
        total_lines += 1
        total_words += len(line.split())
        total_chars += len(line.encode('utf-8'))
    return total_chars, total_lines, total_words


def print_stats(file=None):
    if file:
        lines, words, chars = count_statistics(file)
        print(f"{lines} {words} {chars} {file}")
    else:
        lines, words, chars = count_statistics()
        print(f"{lines} {words} {chars}")
    return lines, words, chars


@click.command()
@click.argument('files', nargs=-1)
def wc(files):
    total_lines = 0
    total_words = 0
    total_chars = 0

    if len(files) == 0:
        print_stats()
    else:
        for filename in files:
            lines, words, chars = print_stats(filename)
            total_lines += lines
            total_words += words
            total_chars += chars

        print(f"{total_lines} {total_words} {total_chars} total")
