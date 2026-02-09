import sys



class CustomException(Exception):
    def __init__(self, error_message: str):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exc_tb = sys.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in file '{self.filename}' at line {self.lineno}: {self.error_message}"



