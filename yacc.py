from ply import yacc

# Get the token map from the lexer.  This is required.
from lexer import Lexical



def logger(p, log):
    print(log, [str(x).replace('\\n', '') for x in p], sep='\t')
    # print([str(qr) for qr in Yacc.quadRuples])
    # print()
    # print(log)
    # pass


class Yacc:
    precedence = (
        ( 'left', 'PLUS', 'MINUS' ),
        ( 'left', 'TIMES', 'DIVIDE' ),
    )

    tokens = Lexical.tokens
    def p_add(self, p ) :
        'expr : expr PLUS expr'
        p[0] = p[1] + p[3]

    def p_sub(self, p ) :
        'expr : expr MINUS expr'
        p[0] = p[1] - p[3]


    def p_mult_div(self, p ) :
        '''expr : expr TIMES expr
                | expr DIVIDE expr'''

        if p[2] == '*' :
            p[0] = p[1] * p[3]
        else :
            if p[3] == 0 :
                print("Can't divide by 0")
                raise ZeroDivisionError('integer division by 0')
            p[0] = p[1] / p[3]

    def p_expr2NUM(self, p ) :
        'expr : NUMBER'
        p[0] = p[1]

    def p_parens(self, p ) :
        'expr : OPENING_PARENTHESES expr CLOSING_PARENTHESES'
        p[0] = p[2]

    def p_error(self, p ):
        print("Syntax error in input!")

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
    