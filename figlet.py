import sys
from pyfiglet import Figlet, figlet_format, FontNotFound


def get_user_input():
    """
    get the user input and strip it from whitespaces
    """
    return input("Input: ").strip()


def valid_font_argument(font_argument):
    """
    check if the font_argument str is -f or --font
    """
    return font_argument in ["-f", "--font"]


def valid_font_name(font_name):
    """
    check if the given font name is valid
    """
    try:
        Figlet(font=str(font_name))
        return True
    except FontNotFound:
        """
        if the given font name is not valid then return False
        """
        return False


def main():
    """
    exclude the file name from the command-line arguments
    """
    args = sys.argv[1:]

    """
    if no font arguments was given in the command-line arguments
    exit the program and print the user input with default Figlet font type
    """
    if not args:
        print(figlet_format(get_user_input()))
        sys.exit(0)

    """
    if font argument and font name was given in the command-line arguments
    """
    if len(args) == 2:
        font_arg, font_name = args
        """
        if the font argument is valid and the font name is also valid
        """
        if valid_font_argument(font_arg) and valid_font_name(font_name):
            """
            exit the program and print the user input with the given font
            """
            print(figlet_format(get_user_input(), font=font_name))
            sys.exit(0)

    """
    exit the programn with the default invalid usage message
    """
    sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
