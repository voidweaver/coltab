#!/usr/bin/env python3

import click
import os

def calculate_foreground(code):
    if code < 8:
        return 15
    elif code < 16:
        return 0
    elif code < 232:
        return 15 if (code - 16) % 36 < 12 else 0
    else:
        return 0 if code > 243 else 15


def get_snippet(code, margin_count, padding_count, pad_char=' '):
    margin = ''
    for _ in range(margin_count):
        margin += ' '

    fg_code = calculate_foreground(code)

    code_string = str(code)
    while len(code_string) < padding_count:
        code_string = pad_char + code_string

    return "\033[38;5;%dm\033[48;5;%dm%s%s%s\033[0m" % (fg_code, code, margin, code_string, margin)


@click.command()
@click.argument('color-code', required=False)
@click.option('-n', '--neighbors', default=0, help='Number of neighbors to display (only works when COLOR_CODE argument is set).')
@click.option('-p', '--no-pointer', is_flag=True, help='Stop showing arrow pointer to the main color snippet.')
@click.option('-h', '--help', 'show_help', is_flag=True, help='Show this message and exit.')
def show_snippets(color_code, neighbors, no_pointer, show_help):
    """A simple script to display samples of 8-bit colors available in most terminals."""
    if show_help:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

    _, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)

    if color_code and color_code.isnumeric() and 0 <= int(color_code) and int(color_code) < 256:
        color_code = int(color_code)
        size = len(str(color_code + neighbors))

        pointer = '\033[1m\033[38;5;9m<----\033[0m'
        for i in range(-neighbors, neighbors + 1):
            snippet = get_snippet(color_code + i, 3, size, '0')
            if i == 0:
                if no_pointer or neighbors < 3:
                    print('\033[1m' + snippet)
                else:
                    print('\033[1m' + snippet, pointer)
            else:
                print(snippet)
    else:
        fourbit_count = 8
        while columns / fourbit_count < 2+2:
            fourbit_count -= 1
        fourbit_width = columns / fourbit_count
        fourbit_width = fourbit_width if fourbit_width < 12 else 12

        line_string = ''
        for i in range(16):
            line_string += get_snippet(i, int((fourbit_width - 2) / 2), 2)
            if i % fourbit_count == fourbit_count - 1:
                print(line_string)
                line_string = ''

        print()

        line_string = ''

        colors_count = 36
        while columns / colors_count < 3+2:
            colors_count -= 18 if colors_count == 36 else 6
        colors_width = columns / colors_count
        
        for i in range(16, 232):
            line_string += get_snippet(i, int((colors_width - 3) / 2), 3)
            if (i - 16) % colors_count == colors_count - 1:
                print(line_string)
                line_string = ''

        print()
        
        greyscale_count = 12
        while columns / greyscale_count < 3+2:
            greyscale_count -= 1
        greyscale_width = columns / greyscale_count
        greyscale_width = greyscale_width if greyscale_width < 12 else 12

        for i in range(232, 256):
            line_string += get_snippet(i, int((greyscale_width - 3) / 2), 3)
            if (i - 232) % greyscale_count == greyscale_count - 1:
                print(line_string)
                line_string = ''


if __name__ == '__main__':
    show_snippets()
