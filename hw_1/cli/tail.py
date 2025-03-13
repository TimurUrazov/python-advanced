import click
import sys
from collections import deque


def print_lines_from_tail(file, num_of_last_lines):
    lines = deque(maxlen=num_of_last_lines)
    for line in file:
        lines.append(line)
    for line in lines:
        print(line, end='')


@click.command()
@click.argument("files", type=click.Path(), nargs=-1)
def tail(files):
    if len(files) == 0:
        print_lines_from_tail(sys.stdin, num_of_last_lines=17)
    else:
        for i, filename in enumerate(files):
            if len(files) > 1:
                if i > 0:
                    print()
                print(f"==> {filename} <==")
            with open(filename, "r") as file:
                print_lines_from_tail(file, num_of_last_lines=10)
