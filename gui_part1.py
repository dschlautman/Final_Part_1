from tkinter import *


class Gui:
    """
    Class representing the GUI application.
    """
    def __init__(self, window) -> None:
        """
        Method to initialize the GUI for the calculator.
        :param window: The main window of the GUI.
        """
        self.window = window

        entry = Entry(window, width=20, font=('Arial', 16), justify='right', state="disabled")
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 1
        col_val = 0

        for button_text in buttons:
            Button(window, text=button_text, width=5, height=2,
                   command=lambda btn=button_text: on_click(btn) if btn != '=' else calculate()).grid(row=row_val,
                                                                                                      column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        def on_click(button_text) -> None:
            """
            Method to handle button clicks for numeric and operator buttons.
            Parameter:
            - button_text (str): The text displayed on the button that was clicked.
            """
            entry.config(state="normal")
            current_text = entry.get()
            new_text = current_text + button_text
            entry.delete(0, END)
            entry.insert(0, new_text)
            entry.config(state="disabled")

        def clear_entry() -> None:
            """
            Method to clear the entry widget.
            """
            entry.config(state="normal")
            entry.delete(0, END)
            entry.config(state="disabled")

        def calculate() -> None:
            """
            Method to calculate when the '=' button is clicked.
            """
            try:
                entry.config(state="normal")
                result = eval(entry.get())
                entry.delete(0, END)
                entry.insert(0, str(result))
                entry.config(state="disabled")
            except Exception as e:
                entry.delete(0, END)
                entry.insert(0, "Error")
                entry.config(state="disabled")

        Button(window, text='Clear', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
