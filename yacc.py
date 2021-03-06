from ply import yacc

# Get the token map from the lexer.  This is required.
from lexer import Lexical

start = 'program'


class Yacc:
    counter = 0
    precedence = (
        ( 'left', 'CLOSING_PARENTHESES'),
        ( 'left', 'OR','LOGICAL_OR','THEN_KW'),
        ( 'left', 'AND','LOGICAL_AND'),
        ( 'left', 'EQUAL'),
        ( 'left', 'LESS_THAN', 'GREATER_THAN', 'LESSEQUAL', 'GREATEREQUAL'),
        ( 'left', 'PLUS', 'MINUS' ),
        ( 'left', 'TIMES', 'DIVIDE' ),
        ( 'left', 'PERCENTAGE' ),
        ( 'left', 'TILDA' ,'PLUSPLUS', 'MINUSMINUS'),
        ( 'nonassoc', 'ELSE_KW'),
    )

    tokens = Lexical.tokens


    def p_program(self, p ) :
        'program : list'
    
    def p_numOrletter_0(self, p ) :
        '''numOrletter : NUMBER'''
    
    def p_numOrletter_1(self, p ) :
        '''numOrletter : VarName'''

    def p_list_0(self, p ) :
        '''list : list declaration'''
            

    def p_list_1(self, p ) :
        '''list : declaration'''
            
    def p_declaration_0(self, p ) :
        '''declaration : function'''
            
            
    def p_declaration_1(self, p ) :
        '''declaration : varDeclaration'''
            
    def p_varDeclaration(self, p ) :
        '''varDeclaration : type variableList SEMICOLON'''
            
    def p_ScopedVariableDec(self, p ):
        '''ScopedVariableDec : scopedSpecifier variableList'''
    
    def p_variableList_0(self, p ):
        '''variableList : variableList COMMA varInitialization'''
    
    def p_variableList_1(self, p ):
        '''variableList : varInitialization'''

    def p_varInitialization_0(self, p ):
        '''varInitialization : varForm'''

    def p_varInitialization_1(self, p ):
        '''varInitialization : varForm DOUBLE_DOT OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES'''

    def p_varForm_0(self, p ) :
        '''varForm : VarName OPENING_BRACKET eachExpression CLOSING_BRACKET'''

    def p_varForm_1(self, p ) :
        '''varForm : VarName'''
    
    def p_scopedSpecifier_0(self, p ) :
        '''scopedSpecifier : STATIC_KW type'''

    def p_scopedSpecifier_1(self, p ) :
        '''scopedSpecifier : type'''

    def p_type_0(self, p ) :
        '''type : BOOLEAN_KW'''

    def p_type_1(self, p ) :
        '''type : CHARACTER_KW'''

    def p_type_2(self, p ) :
        '''type : INTEGER_KW'''

    def p_type_3(self, p ) :
        '''type : CHAR_KW '''

    def p_type_4(self, p ) :
        '''type : BOOL_KW'''

    def p_type_5(self, p ) :
        '''type : INT_KW'''

    def p_function_0(self, p ) :
        '''function : VOID_KW FuncName OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE statement CLOSING_BRACE'''
    
    def p_function_1(self, p ) :
        '''function : VOID_KW VarName OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE statement CLOSING_BRACE'''
    
    def p_function_2(self, p ) :
        '''function : type FuncName OPENING_PARENTHESES parameter CLOSING_PARENTHESES statement'''
    
    def p_function_3(self, p ) :
        '''function : type VarName OPENING_PARENTHESES parameter CLOSING_PARENTHESES statement'''
    
    def p_parameter_0(self, p ) :
        '''parameter : listOfParameters'''
    
    def p_parameter_1(self, p ) :
        '''parameter : empty'''

    def p_listOfParameters_0(self, p ) :
        '''listOfParameters : listOfParameters SEMICOLON paramTypeList'''
    

    def p_listOfParameters_1(self, p ) :
        '''listOfParameters : paramTypeList'''
    
    def p_paramTypeList(self, p ) :
        '''paramTypeList : type paramList'''
    
    def p_paramList_0(self, p ) :
        '''paramList : paramList COMMA paramId'''
    
    def p_paramList_1(self, p ) :
        '''paramList : paramId'''

    def p_localDeclarations_0(self, p ) :
        '''localDeclarations : localDeclarations ScopedVariableDec'''

    def p_localDeclarations_1(self, p ) :
        '''localDeclarations : empty'''

    def p_paramId_0(self, p ) :
        '''paramId : VarName'''

    def p_paramId_1(self, p ) :
        '''paramId : VarName OPENING_BRACKET CLOSING_BRACKET'''

    def p_core_statement_0(self, p ) :
        '''core_statement : matched
        | unmatched
        '''
    
    def p_matched(self, p ) :
        '''matched : IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES matched OTHER_KW matched
        | IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES OPENING_BRACE matched CLOSING_BRACE OTHER_KW matched
        | statement
        '''

    def p_unmatched(self, p ) :
        '''unmatched : IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES matched
        |   IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES OPENING_BRACE matched CLOSING_BRACE
        |   IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES matched OTHER_KW unmatched
        |   IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES OPENING_BRACE matched CLOSING_BRACE OTHER_KW unmatched
        '''

    def p_statement_0(self, p ) :
        '''statement : phrase'''

    def p_statement_1(self, p ) :
        '''statement : compoundPhrase'''

    def p_statement_3(self, p ) :
        '''statement : iterationPhrase'''

    def p_statement_4(self, p ) :
        '''statement : returnPhrase'''

    def p_statement_5(self, p ) :
        '''statement : continue'''

    def p_compoundPhrase(self, p ) :
        '''compoundPhrase : OPENING_BRACE localDeclarations statementList CLOSING_BRACE'''
    
    def p_statementList_0(self, p ) :
        '''statementList : statementList statement'''
    
    def p_statementList_1(self, p ) :
        '''statementList : empty'''
    
    def p_phrase_0(self, p ) :
        '''phrase : allExpression SEMICOLON'''
    
    def p_phrase_1(self, p ) :
        '''phrase : SEMICOLON'''

    def p_ifBody_0(self, p ) :
        '''ifBody : matched'''

    def p_ifBody_1(self, p ) :
        '''ifBody : matched OTHER_KW matched'''

    def p_iterationPhrase(self, p ) :
        '''iterationPhrase : TILL_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statement'''
        
    def p_returnPhrase_0(self, p ) :
        '''returnPhrase : COMEBACK_KW SEMICOLON'''
        
    def p_returnPhrase_1(self, p ) :
        '''returnPhrase : GIVEBACK_KW allExpression SEMICOLON'''
        
    def p_continue(self, p ) :
        '''continue : CONTINUE_KW SEMICOLON'''

    def p_allExpression_0(self, p):
        '''allExpression : alterable mathOp allExpression'''
     
    def p_allExpression_1(self, p):
        '''allExpression : alterable PLUSPLUS'''
     
    def p_allExpression_2(self, p):
        '''allExpression : alterable MINUSMINUS'''
     
    def p_allExpression_3(self, p):
        '''allExpression : eachExpression'''

    def p_allExpression_4(self, p):
        '''allExpression : alterable mathOp NUMBER'''
     
    def p_mathOp_0(self, p):
        '''mathOp : EQUAL'''
    
    def p_mathOp_1(self, p):
        '''mathOp : PLUSEQUAL'''
    
    def p_mathOp_2(self, p):
        '''mathOp : MINUSEQUAL'''
    
    def p_mathOp_3(self, p):
        '''mathOp : TIMESEQUAL'''
    
    def p_mathOp_4(self, p):
        '''mathOp : DIVIDEEQUAL'''

    def p_eachExpression_0(self, p):
        '''eachExpression : eachExpression LOGICAL_AND eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_1(self, p):
        '''eachExpression : eachExpression LOGICAL_AND THEN_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_3(self, p):
        '''eachExpression : eachExpression LOGICAL_AND ELSE_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_4(self, p):
        '''eachExpression : eachExpression LOGICAL_OR eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_5(self, p):
        '''eachExpression : eachExpression LOGICAL_OR THEN_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_7(self, p):
        '''eachExpression : eachExpression LOGICAL_OR ELSE_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_100(self, p):
        '''eachExpression : unaryEachExpression'''

    def p_eachExpression_101(self, p):
        '''unaryEachExpression : TILDA eachExpression'''
        print('#',self.counter,'\t',p[1],'\t',p[2],'\t')
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_12(self, p):
        '''eachExpression : eachExpression AND eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_13(self, p):
        '''eachExpression : eachExpression AND THEN_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_15(self, p):
        '''eachExpression : eachExpression AND ELSE_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_16(self, p):
        '''eachExpression : eachExpression OR eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_17(self, p):
        '''eachExpression : eachExpression OR THEN_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_eachExpression_19(self, p):
        '''eachExpression : eachExpression OR ELSE_KW eachExpression'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1
    
    def p_eachExpression_20(self, p):
        '''eachExpression : relExpression'''
        p[0] = p[1]
    
    def p_relExpression_0(self, p):
        '''relExpression : mathEXP compareType mathEXP'''
    
    def p_relExpression_1(self, p):
        '''relExpression : mathEXP'''
        p[0] = p[1]
    
    def p_compareType_0(self, p):
        '''compareType : equal'''
    
    def p_compareType_1(self, p):
        '''compareType : nonEqual'''
    
    def p_equal_0(self, p):
        '''equal : LESSEQUAL'''
    
    def p_equal_1(self, p):
        '''equal : GREATEREQUAL'''
    
    def p_equal_2(self, p):
        '''equal : EQUALEQUAL'''
    
    def p_nonEqual_0(self, p):
        '''nonEqual : LESS_THAN'''
    
    def p_nonEqual_1(self, p):
        '''nonEqual : GREATER_THAN'''
    
    def p_nonEqual_2(self, p):
       '''nonEqual : NOTEQUAL'''
    
    def p_mathEXP_0(self, p ) :
        '''mathEXP : mathEXP PLUS mathEXP'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_mathEXP_1(self, p ) :
        '''mathEXP : mathEXP MINUS mathEXP'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_mathEXP_2(self, p ) :
        '''mathEXP : mathEXP TIMES mathEXP'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_mathEXP_3(self, p ) :
        '''mathEXP : mathEXP DIVIDE mathEXP'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1

    def p_mathEXP_4(self, p ) :
        '''mathEXP : mathEXP PERCENTAGE mathEXP'''
        print('#',self.counter,'\t',p[2],'\t',p[1],'\t',p[3])
        p[0] = '('+str(self.counter)+')'
        self.counter += 1
    
    def p_mathEXP_5(self, p ) :
        '''mathEXP : unaryExpression'''
        p[0] = p[1]

    def p_unaryExpression_0(self, p ) :
        '''unaryExpression : unaryop unaryExpression'''
        p[0] = p[1]
    
    def p_unaryExpression_1(self, p ) :
        '''unaryExpression : factor'''
        p[0] = p[1]
    
    def p_unaryop_0(self, p ) :
        '''unaryop : MINUS'''

    def p_unaryop_1(self, p ) :
        '''unaryop : TIMES'''

    def p_unaryop_2(self, p ) :
        '''unaryop : QUESTION_MARK'''

    def p_factor_0(self, p):
        '''factor : inalterable'''
    
    def p_factor_1(self, p):
        '''factor : alterable'''
        p[0] = p[1]

    def p_alterable_0(self, p):
        '''alterable :  VarName'''
        p[0] = p[1]

    def p_alterable_1(self, p):
        '''alterable : alterable OPENING_BRACKET allExpression CLOSING_BRACKET'''

    def p_alterable_2(self, p):
        '''alterable : alterable DOT VarName'''

    def p_inalterable_0(self, p):
        '''inalterable : OPENING_PARENTHESES allExpression CLOSING_PARENTHESES'''

    def p_inalterable_1(self, p):
        '''inalterable : constant'''

    def p_inalterable_2(self, p):
        '''inalterable : VarName OPENING_PARENTHESES args CLOSING_PARENTHESES'''

    def p_args_0(self, p):
        '''args : arguments'''

    def p_args_1(self, p):
        '''args : empty'''

    def p_arguments_0(self, p):
        '''arguments : arguments COMMA allExpression'''

    def p_arguments_1(self, p):
        '''arguments : allExpression'''

    def p_constant_0(self, p):
        '''constant : CONST_KW'''

    def p_constant_1(self, p):
        '''constant : TRUE_KW'''

    def p_constant_2(self, p):
        '''constant : FALSE_KW'''

    def p_empty(self, p):
        """
        empty :
        """
        
    def p_error(self, p ):
        print(p)
        print("Syntax error in input!")

    def build(self, **kwargs):
        """
        build the parser
        """
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
    