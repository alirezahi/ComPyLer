from lexer import Lexical
from yacc import Yacc
data = '''
a = 2 ;
'''
l = Lexical()
y = Yacc()
r = y.build().parse(data,l.build(),False)
print(r)