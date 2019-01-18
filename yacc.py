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

    def p_program(self, p ) :
        'program : list'

    def p_list(self, p ) :
        '''list : list declaration
                | declaration'''
            
    def p_declaration(self, p ) :
        '''declaration : function
                | varDeclaration'''
            
    def p_varDeclaration(self, p ) :
        '''varDeclaration : type variableList
                | varDeclaration'''
            
    def p_ScopedVariableDec(self, p ) :
        '''ScopedVariableDec : scopedSpecifier variableList'''
    
    def p_variableList(self, p ) :
        '''p_variableList : p_variableList COMMA varInitialization
                        |   varInitialization'''

    def p_varInitialization(self, p ) :
        '''varInitialization : varForm | varForm DOUBLE_DOT OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES'''

    def p_varForm(self, p ) :
        '''varForm : LETTER | numOrLetter OPENING_BRACKET NUMBER CLOSING_BRACKET'''

    def p_scopedSpecifier(self, p ) :
        '''scopedSpecifier : STATIC_KW type | type'''

    def p_type(self, p ) :
        '''type : BOOLEAN_KW | CHARACTER_KW | INTEGER_KW | CHAR_KW | BOOL_KW | INT_KW'''

    def p_function(self, p ) :
        '''function : VOID_KW
        |   numOrLetter OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE statement CLOSING_BRACE
        |   type LETTER numOrLetter OPENING_PARENTHESES parameter CLOSING_PARENTHESES statement'''
    
    def p_parameter(self, p ) :
        '''parameter : listOfParameters | ε'''

    def p_listOfParameters(self, p ) :
        '''listOfParameters : listOfParameters SEMICOLON paramTypeList | paramTypeList'''
    
    def p_paramTypeList(self, p ) :
        '''paramTypeList : type paramList'''
    
    def p_paramList(self, p ) :
        '''paramList : paramList COMMA paramId | paramId'''

    def p_localDeclarations(self, p ) :
        '''localDeclarations : localDeclarations ScopedVariableDec | ε'''

    def p_paramId(self, p ) :
        '''paramId : LETTER numOrLetter | LETTER numOrLetter OPENING_BRACKET CLOSING_BRACKET'''

    def p_statement(self, p ) :
        '''statement : phrase | compoundPhrase | selectPhrase | iterationPhrase | returnPhrase | continue'''

    # def p_compoundPhrase(self, p ) :
    #     '''compoundPhrase : OPENING_BRACE localDeclarations statementList CLOSING_BRACE'''
    
    def p_statementList(self, p ) :
        '''statementList : statementList statement | ε'''
    
    # def p_phrase(self, p ) :
    #     '''phrase : allExpression SEMICOLON | SEMICOLON'''
    
    # def p_selectPhrase(self, p ) :
    #     '''selectPhrase : IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES ifBody
    #     |   IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES OPENING_BRACE ifBody ifBody CLOSING_BRACE
    #     '''

    # def p_ifBody(self, p ) :
    #     '''ifBody : statement | statement OTHER_KW statement | SEMICOLON'''

    # def p_iterationPhrase(self, p ) :
    #     '''iterationPhrase : till OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statement'''
        
    # def p_returnPhrase(self, p ) :
    #     '''returnPhrase : COMEBACK_KW SEMICOLON
    #     |   GIVEBACK_KW allExpression SEMICOLON
    #     |   GIVEBACK_KW numOrLetter SEMICOLON'''

    # def p_continue(self, p ) :
    #     '''continue : CONTINUE SEMICOLON'''

    # def p_continue(self, p ) :
    #     '''continue : CONTINUE SEMICOLON'''





    def p_mathEXP(self, p ) :
        '''mathEXP : mathEXP op mathEXP | unaryExpression'''

    # def p_op(self, p ) :
    #     '''op : PLUS | MINUS | TIMES | DIVIDE | PERCENTAGE'''

    def p_unaryExpression(self, p ) :
        '''unaryExpression : unaryop unaryExpression | factor'''
    
    # def p_unaryop(self, p ) :
    #     '''unaryop : MINUS | TIMES | QUESTION_MARK'''

    def p_error(self, p ):
        print("Syntax error in input!")

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
    