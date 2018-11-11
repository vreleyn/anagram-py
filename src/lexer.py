# The main code for the lexer 

class Lexer:
    def __init__(self, code):
        self.code = code
        self.index = 0

    def __str__(self):
        return "Lexer with code: (" + self.code.__str__() + ")"

    def isdigit(self, char):
        return char >= '0' and char <= '9'

    def isletter(self, char):
        return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')

    def isalnum(self, char):
        return self.isdigit(char) or self.isletter(char)

    def get_token(self, index):
        char = ''
        while(self.get_char(self.code, index).isspace()):
            index += 1
        char = self.get_char(self.code, index)
        if self.isdigit(char):
            return (index, self.get_match_token(index, self.isdigit))
        elif self.isletter(char):
            return (index, self.get_match_token(index, self.isalnum))
        else:
            return (index, Token(char, "file", 0, 0))
        return token

    def get_next_token(self):
        t = self.get_token(self.index)
        self.index += len(t.value)
        return t

    def get_char(self, code, index):
        return code[index] if len(code) > index else chr(0)

    def get_match_token(self, index, fn):
        length = 0
        while(fn(self.get_char(self.code, index+length))):
            length = length + 1
        return Token(self.code[index:index+length], "file", 0, 0)
               
    def get_tokens(self):
        tokens = []
        index = 0
        while(index < len(self.code)):
            (index, token) = self.get_token(index)
            index += len(token.value)
            tokens.append(token)
        return tokens


class Token:
    def __init__(self, value, fname, line, col):
        self.position = "(" + fname.__str__() + " at " + line.__str__() + ":" + col.__str__() + ")"
        self.value = value

    def __str__(self):
        return '{' + self.value.__str__() + " " + self.position.__str__() + '}'

    def str(self):
        return self.__str__()
