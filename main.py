from lexer import Lexical
from yacc import Yacc
data = '''
3+4
'''
l = Lexical()
y = Yacc()
r = y.build().parse(data,l.build(),False)
print(r)