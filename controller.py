class Controller:
    def __init__(self, model, display):
        self.model = model
        self.display = display

    def import_wav(self):
        """
        Sets the file to import
        :return:
        """

        try:
            # import the model
            self.model.import_wav()
            # show a success message
            self.display.show_success(f'File {self.model.filepath} has been imported.')
        except ValueError as error:
            # show an error message
            self.display.show_error(error)

