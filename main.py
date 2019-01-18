from lexer import Lexical
from yacc import Yacc
data = '''
if(B < A){;}
'''
l = Lexical()
y = Yacc()
r = y.build().parse(data,l.build(),False)
print(r)