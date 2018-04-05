# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Compilers Design
# Lexical Specification of Project:
# Rust interpreter with Python
# -----------------------------------------------------------------------------

import rust_lex as lexer

# Node class to manage the nodes and children
class Node:
    def __init__(self, token, value=None, node_type=None, children=None):
            self.token = token
            self.value = value
            self.node_type = ntype
            if children:
                self.children = children
            else:
                self.children = []

    def get_values(self):
        return '"' + self.token + ':' + str(self.value) + ':' + \
                str(self.node_type) + '"'

    def debug(self):

        if self.children:
            for child in self.children:
                print(self.get_values(), '->', child.get_values())
                child.debug()

# Bring the tokens from the lexer
tokens = lexer.tokens

# -----------------------------------------------------------------------------
# Parsing Rules
# -----------------------------------------------------------------------------

"""
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)
"""

# Dictionary of names
names = {}

def p_foo(p):
    """
    foo : program
    """
    pass

# Rule to run program
def p_program(p):
    """
    program : declarationList
    """
    p[0] = Node("program", None, None, [p[1]])
    p[0].debug()
    print("\n")

# Rule for general statement
def p_general(p):
    """
    general : stmt
            | stmt general
    """
    pass

# Rule to implement statements
def p_stmt(p):
    """
    stmt : expressionStmt
         | declaration
         | selectionStmt
         | iterationStmt
         | inputStmt
         | outputStmt
    """
    pass

# Rule to implement several declarations
def p_declarationList(p):
    """
    declarationList : declaration
                    | declaration declarationList
    """
    if len(p) == 2:
        p[0] = Node("declaration-list", None, None, [p[1]])
    else:
        p[0] = Node("declaration-list", None, None, [p[1], p[2]])

# Rule to implement single declaration
def p_declaration(p):
    """
    declaration : varDeclaration
                | constDeclaration
                | staticDeclaration
                | funcDeclaration
    """
    p[0] = Node("declaration", None, None, [p[1]])

# Rule to implement variable declaration
def p_varDeclaration(p):
    """
    varDeclaration : LET IDVAR EQUAL IDVAR SEMCL
                   | LET IDVAR EQUAL INTVR SEMCL
                   | LET IDVAR EQUAL expressionStmt SEMCL
    """
    if len(p) == 6:
        p[0] = Node('varDeclaration', [p[2], p[2]], None, None)
    else:
        p[0] = Node('varDeclaration', [p[2]], None, None)

# Rule to implement constant declaration
def p_constDeclaration(p):
    """
    constDeclaration : CONST IDVAR EQUAL IDVAR SEMCL
    """
    pass

# Rule to implement static declaration
def p_staticDeclaration(p):
    """
    staticDeclaration : STATIC IDVAR EQUAL IDVAR SEMCL
    """
    pass

# Rule to implement function declarations
def p_funcDeclaration(p):
    """
    funcDeclaration : FN function
    """
    T = Node("FN")
    p[0] = Node("function-declaration", None, None, [T, p[2]])

# Rule to implement functions
def p_function(p):
    """
    function : FN parameters block
    """
    T = Node("FN", p[1])
    p[0] = Node("function", None, None, [T, p[2], p[3]])

# Rule to implement parameters for functions
def p_parameters(p):
    """
    parameters : OPENP CLOSP
               | OPEN paramList CLOSP
    """
    T1 = Node("OPENP", p[1])
    if (len(p) == 3):  # First case
        T2 = Node("CLOSP", p[2])
        p[0] = Node("parameters", None, None, [T1, T2])
    else:
        T2 = Node("RPAREN", p[3])
        p[0] = Node("parameters", None, None, [T1, T2, p[2]])

# Rule to implement parameter list
def p_paramList(p):
    """
    paramList : parameter
              | parameter COMMA paramList
    """
    if len(p) == 2:
        p[0] = Node('parameter-list', None, None, [p[1]])
    else:
        T = Node('COMMA', p[2])
        p[0] = Node('parameter-list', None, None, [p[1], T, p[3]])

# Rule to implement expressions
def p_expressionStmt(p):
    """expressionStmt : expression
    """
    pass

# Rule to implement iterations
def p_iterationStmt(p):
    """
    iterationStmt : FOR IDVAR IN expression
                  | WHILE expression EQLTO general
                  | WHILE expression LESST general
                  | WHILE expression GREAT general
    """
    pass

# Rule to implement iterations
def p_selectionStmt(p):
    """
    selectionStmt : IF expression EQUAL general
                  | IF expression EQUAL general ELSE
    """
    pass

# Rule for general expression
def p_expression(p):
    """
    expression : expression OROPE andExpr
               | andExpr
    """
    pass

# Rule for AND expression
def p_andExpr(p):
    """
    andExpr : andExpr ANDOP relExpr
            | relExpr
    """
    pass

# Rule for regular expression
def p_rel_expr(p):
    """
    relExpr : sumExpr relop sumExpr
    """
    pass

# Rule for operators
def p_relop(p):
    """
    relop : LESST
          | LSSEQ
          | GREAT
          | GRTEQ
          | EQUAL
          | UNEQL
          | EQLTO
    """
    pass

# Rule for sum expression
def p_sumExpr(p):
    """
    sumExpr : sumExpr sumOp term
            | term
    """
    pass

# Rule for sum operator
def p_sumOp(p):
    """
    sumOp : ADDOP
          | SUBOP
    """
    pass

# Rule for terms
def p_term(p):
    """
    term : term mulOp number
         | number
    """
    pass

# Rule to implement numbers
def p_number(p):
    """
    number : INTVR
    """
    pass

# Rule for multiplication and division operator
def p_mulOp(p):
    """
    mulOp : DEROP
          | QUOOP
    """
    pass

# Rule for inputs
def p_input_stmt(p):
    """
    inputStmt : STDIN OPENP stmt CLOSP
    """
    pass

# Rule for outputs
def p_output_stmt(p):
    """
    outputStmt : PRINTLN OPENP stmt CLOSP
    """
    pass

# Rule for booleans
def p_booleans(p):
    """
    booleans : LET IDVAR EQUAL TRUE
             | LET IDVAR EQUAL FALSE
    """
    pass

# Rule for Catastrophic error
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Import yacc
import ply.yacc as yacc
parser = yacc.yacc(start='foo')
