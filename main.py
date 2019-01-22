from lexer import Lexical
from yacc import Yacc
data = '''
int a : (t + q + r - y * e && ~ y * e) ;
void asd(){
    a ++;
}
'''
l = Lexical()
y = Yacc()
r = y.build().parse(data,l.build(),False)
print(r)