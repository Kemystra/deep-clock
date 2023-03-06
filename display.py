import curses
import logging

"""
It should be expected that the color_number be fixed here.
It is the responsibility of the user to customizes what
color_number represents *what*.
"""


CHAR_TO_INDEX = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    ':': 10,
}


def display_text(screen, text, x, y, attrs=[]):
    # OR with initial color
    additional_attr = curses.color_pair(1)
    for attr in attrs:
        additional_attr |= attr

    screen.addstr(y, x, text, additional_attr)
    screen.refresh()


def display_custom_font(screen, text, x, y):
    # Get the characters list
    custom_font_text = concat_custom_font_char(text)

    for i, line in enumerate(custom_font_text):
        # A newline would simply start the line at the START
        # So we set each line with the appropriate x-value
        # And incrementing the y-value for each subsequent line
        screen.addstr(y + i, x, line, curses.color_pair(1))

    # Refresh after every line has been drawn
    screen.refresh()
    

# Get numbers
def get_chars_from_file():
    char_pack = []

    with open("characters.txt") as f:
        content = f.read()
        res = []
        num_char = ""
        for c in content:
            if c == '.':
                num_char += ' '
            elif c == '#':
                num_char += '\u2588'
            elif c == '\n' and num_char != '':
                res.append(num_char)
                num_char = ""
            elif c == '=':
                char_pack.append(res)
                res = []
                num_char = ""

    return char_pack


def concat_custom_font_char(string):
    characters = get_chars_from_file()
    separated_chars = [characters[CHAR_TO_INDEX[x]] for x in string]

    complete_lines = []
    for i in range(len(separated_chars[0])):
        line = ' '.join(ch[i] for ch in separated_chars)
        complete_lines.append(line)

    return complete_lines