# STRINGS WITH CIRCUMFLEX
from strings_with_circumflex import string_with_circumflex

##############
### ERRORS ###
##############

class Error:
    def __init__(self, position_start, position_end, error_name, error_details):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.error_details = error_details

    def as_string(self):
        result = f'{self.error_name}: {self.error_details}\n'
        result += f'File {self.position_start.file_name}, line {self.position_start.ln + 1}'
        result += '\n\n' + string_with_circumflex(self.position_start.file_txt, self.position_start, self.position_end)
        return result

class IllegalCharError(Error):
    def __init__(self, position_start, position_end, error_details):
        super().__init__(position_start, position_end, 'Illegal Character', error_details)

class InvalidSyntaxError(Error):
    def __init__(self, position_start, position_end, error_details = ''):
        super().__init__(position_start, position_end, 'Invalid Syntax', error_details)