import ply.lex as lex
 
 # List of token names.   This is always required

class Lexical():
    symbol_table = []

    tokens = (
    'ID',
    'NUMBER',
    'OPENING_BRACKET',
    'CLOSING_BRACKET',
    'OPENING_PARENTHESES',
    'CLOSING_PARENTHESES',
    'OPENING_BRACE',
    'CLOSING_BRACE',
    'PLUSPLUS',
    'MINUSMINUS',
    'EQUAL',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'TIMESEQUAL',
    'DIVIDEEQUAL',
    'LESSEQUAL',
    'GREATEREQUAL',
    'EQUALEQUAL',
    'LESS_THAN',
    'GREATER_THAN',
    'NOTEQUAL',
    'SEMICOLON',
    'COLON',
    'DOT',
    'DOUBLE_DOT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PERCENTAGE',
    'QUESTION_MARK',
    'LOGINCAL_AND',
    'LOGINCAL_OR',
    'TILDA',
    'AND',
    'OR',
    'STATIC_KW',
    'BOOLEAN_KW',
    'CHARACTER_KW',
    'INTEGER_KW',
    'CHAR_KW',
    'BOOL_KW',
    'INT_KW',
    'VOID_KW',
    'IF_KW',
    'OTHER_KW',
    'TILL_KW',
    'COMEBACK_KW',
    'GIVEBACK_KW',
    'CONTINUE_KW',
    'THEN_KW',
    'ELSE_KW',
    'CONST_KW',
    'TRUE_KW',
    'FALSE_KW',
    )

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_PLUSPLUS  = r'\+\+'
    t_MINUSMINUS  = r'\-\-'
    t_EQUAL  = r'='
    t_PLUSEQUAL  = r'\+='
    t_MINUSEQUAL  = r'-='
    t_TIMESEQUAL  = r'\*='
    t_DIVIDEEQUAL  = r'/='
    t_LESSEQUAL  = r'<='
    t_GREATEREQUAL  = r'>='
    t_EQUALEQUAL  = r'=='
    t_LESS_THAN  = r'<'
    t_GREATER_THAN  = r'>'
    t_NOTEQUAL  = r'\!='
    t_SEMICOLON  = r';'
    t_COLON  = r','
    t_PERCENTAGE  = r'%'
    t_QUESTION_MARK  = r'\?'
    t_LOGINCAL_AND  = r'&&'
    t_LOGINCAL_OR  = r'\|\|'
    t_TILDA  = r'~'
    t_AND  = r'and'
    t_OR  = r'or'
    t_DOT = r'\.'
    t_DOUBLE_DOT  = r':'
    t_OPENING_BRACKET = r'\['
    t_CLOSING_BRACKET = r'\]'
    t_OPENING_PARENTHESES = r'\('
    t_CLOSING_PARENTHESES = r'\)'
    t_OPENING_BRACE = r'\{'
    t_CLOSING_BRACE = r'\}'

    reserved = {
        'static': 'STATIC_KW',
        'boolean': 'BOOLEAN_KW',
        'character': 'CHARACTER_KW',
        'integer': 'INTEGER_KW',
        'char': 'CHAR_KW',
        'bool': 'BOOL_KW',
        'int': 'INT_KW',
        'void': 'VOID_KW',
        'if': 'IF_KW',
        'other': 'OTHER_KW',
        'till': 'TILL_KW',
        'comeback': 'COMEBACK_KW',
        'comeBack': 'COMEBACK_KW',
        'giveback': 'GIVEBACK_KW',
        'giveBack': 'GIVEBACK_KW',
        'continue': 'CONTINUE_KW',
        'then': 'THEN_KW',
        'else': 'ELSE_KW',
        'const': 'CONST_KW',
        'true': 'TRUE_KW',
        'false': 'FALSE_KW',
    }

    def t_ID(self, t):
        r'[0-9]*[a-zA-Z]+[0-9a-zA-Z]*'
        t.type = self.reserved.get(t.value, 'ID')
        if t.type == 'ID':
            self.symbol_table.append(t.value)
        return t


    def t_NUMBER(self, t):
        r'[1-9]+[0-9]*'
        return t


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        lexer = lex.lex(module=self,**kwargs)





        # Test it out
        data = '''
        void 1secondFunc(bool B ; int A ) { int firstArray [5] ;
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

        # Give the lexer some input
        lexer.input(data)
        
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok)
        print(self.symbol_table)

l = Lexical()
l.build()