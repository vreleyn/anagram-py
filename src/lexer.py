# The main code for the lexer 

class Lexer:
    def __init__(self, code):
        self.code = code
        self.index = 0

    def __str__(self):
        return "Lexer with code: (" + self.code.__str__() + ")"

    def isdigit(self, char):
        return char >= '0' and char <= '9'

    def get_token(self, index):
        char = self.get_char(self.code, index)
        if char >= '0' and char <= '9':
            return self.get_match_token(index, self.isdigit)
        else:
            return None
        return token

    def get_char(self, code, index):
        return code[index] if len(code) > index else chr(0)

    def get_match_token(self, index, fn):
        length = 0
        while(fn(self.get_char(self.code, index+length))):
            length = length + 1
        return Token(self.code[index:index+length], "file", 0, 0)
               
    def get_tokens(self):
        return None


class Token:
    def __init__(self, value, fname, line, col):
        self.position = "(" + fname.__str__() + " at " + line.__str__() + ":" + col.__str__() + ")"
        self.value = value

    def __str__(self):
        return '{' + self.value.__str__() + " " + self.position.__str__() + '}'
