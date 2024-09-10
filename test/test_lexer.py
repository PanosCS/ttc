from unittest import TestCase

from lexer import Lexer


class TestLexer(TestCase):

    def setUp(self):
        super().setUp()
        self.lexer = Lexer("Test me daddy")

    def test_next_char(self):
        self.assertEquals(self.lexer.cur_char, 'T')
        self.lexer.next_char()
        self.assertEquals(self.lexer.cur_char, 'e')

    def test_peek(self):
        self.fail()

    def test_abort(self):
        self.fail()

    def test_skip_whitespace(self):
        self.fail()

    def test_skip_comment(self):
        self.fail()

    def test_get_token(self):
        self.fail()
