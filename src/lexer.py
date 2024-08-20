from enum import Enum


class Lexer:
    def __init__(self, source):
        self.source = source + '\n'  # Source code to lex as a string. Append a newline to simplify lexing/parsing the last token/statement.
        self.cur_char = ''  # Current character in the string.
        self.cur_pos = -1  # Current position in the string.
        self.next_char()

    # Process the next character.
    def next_char(self) -> None:
        self.cur_pos += 1
        if self.cur_pos >= len(self.source):
            self.cur_char = '\0'  # EOF
        else:
            self.cur_char = self.source[self.cur_pos]

    # Return the lookahead character.
    def peek(self) -> str:
        if self.cur_pos + 1 >= len(self.source):
            return '\0'  # EOF
        return self.source[self.cur_pos + 1]

    # Invalid token found, print error message and exit.
    def abort(self, message):
        pass

    # Skip whitespace except newlines, which we will use to indicate the end of a statement.
    def skip_whitespace(self):
        pass

    # Skip comments in the code.
    def skip_comment(self):
        pass

    # Return the next token.
    def get_token(self):
        # Check the first character of this token to see if we can decide what it is.
        # If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest.
        if self.cur_char == '+':
            pass  # Plus token.
        elif self.cur_char == '-':
            pass  # Minus token.
        elif self.cur_char == '*':
            pass  # Asterisk token.
        elif self.cur_char == '/':
            pass  # Slash token.
        elif self.cur_char == '\n':
            pass  # Newline token.
        elif self.cur_char == '\0':
            pass  # EOF token.
        else:
            # Unknown token!
            pass

        self.next_char()

# Token contains the original text and the type of token.
class Token:
    def __init__(self, token_text, token_kind):
        self.text = token_text   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = token_kind   # The TokenType that this token is classified as.


# TokenType is our enum for all the types of tokens.
class TokenType(Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # Operators.
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211