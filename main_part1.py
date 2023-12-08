from gui_part1 import *


def main() -> None:
    """
    Main function to initialize and run the GUI for the Final Project.
    """
    window = Tk()
    window.title("Final Project Calculator")
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
