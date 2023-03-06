class Font:
    def __init__(self, font_lines):
        self.font_lines = font_lines


def Font(font_lines="", filename=""):
    if font_lines:
        return Font(font_lines)
    elif filename:
        pass
    else:
        raise AttributeError("class 'Font' requires either a file name or a 2D list of characters")