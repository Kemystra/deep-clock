import curses
import time
import logging

# Relative scripts
import display
from stopwatch import Stopwatch
import constants

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s",
    filename=".log",
    filemode="w"
)

def main(std_screen):

    # Initialization
    curses.curs_set(0)
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_GREEN, -1)

    # Make sure that the screen don't wait for user input
    # i.e: non-blocking mode
    std_screen.nodelay(True)

    # Get height and width
    height, width = std_screen.getmaxyx()

    # Get centered coordinate
    centered_y = (height - len(custom_font_text)) // 2
    centered_x = (width - len(custom_font_text[0])) // 2

    # Instantiate and start a new Stopwatch object
    watch = Stopwatch()
    watch.start()

    display.display_text(
        std_screen, constants.TITLE_TEXT,
        (width - len(constants.TITLE_TEXT)) // 2,
        constants.TITLE_Y_POS
    )

    while True:
        if not watch.is_paused():
            # Convert Unix timestamp into Python's time_struct, then into string
            time_struct = time.gmtime(watch.get_elapsed_time())
            time_string = time.strftime("%H:%M:%S", time_struct)

            display.display_custom_font(
                std_screen, time_string,
                centered_x, centered_y
            )
        
        # Main keystroke handling
        c = std_screen.getch()
        if c == ord('p'):
            if not watch.is_paused():
                logging.info("Paused")
                watch.pause()
            else:
                logging.info("Resumed")
                watch.resume()
        elif c == ord('q'):
            break

        time.sleep(constants.MAIN_LOOP_SLEEP_DURATION)


if __name__ == "__main__":
    curses.wrapper(main)