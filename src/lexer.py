# The main code for the lexer 

class Lexer:
    def __init__(self, code):
        self.code = code
        self.index = 0

    def __str__(self):
        return "Lexer with code: (" + self.code.__str__() + ")"

    def get_token(self, index):
        return None

    def get_tokens(self):
        return None


class Token:
    def __init__(self, value, fname, line, col):
        self.position = "(" + fname.__str__() + " at " + line.__str__() + ":" + col.__str__() + ")"
        self.value = value

    def __str__(self):
        return '{' + self.value.__str__() + " " + self.position.__str__() + '}'
