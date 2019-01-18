from lexer import Lexical
data = '''
//void 1secondFunc(bool B ; int A ) { int firstArray [5] ;
bool A1 ;
bool A2 ;
A1= firstNum <= secondNum A2 = B ;
if ( A1 and Then A2 ) continue ;
Other
{
int B1 ;
if (B1<5) till(B1 != 5) B1++;
If (B1== A) A2 = false; } comeBack; }
'''
l = Lexical()
l.build(data=data)