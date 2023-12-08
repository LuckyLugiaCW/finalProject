import tkinter as tk
from tkinter import ttk


class Display(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # save button
        self.import_button = ttk.Button(self, text='Import', command=self.import_clicked)
        self.import_button.grid(row=1, column=0, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=0)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """

        self.controller = controller

    def import_clicked(self):
        """
        Handle button click event
        :return:
        """

        if self.controller:
            self.controller.import_wav()

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """

        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """

        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

    def hide_message(self):
        """
        Hide the message
        :return:
        """

        self.message_label['text'] = ''


