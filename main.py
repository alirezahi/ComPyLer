from lexer import Lexical
from yacc import Yacc
data = '''
int ae2e, b23d  ;
void asd(){
    ;
}
'''
l = Lexical()
y = Yacc()
r = y.build().parse(data,l.build(),False)
print(r)