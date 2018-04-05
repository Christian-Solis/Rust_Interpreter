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
    pass
    # p[0] = Node("program", None, None, [p[1]])
    # p[0].debug()
    # print("\n")

# # Rule for general statement
# def p_general(p):
#     """
#     general : stmt
#             | stmt general
#     """
#     pass

# Rule to implement several declarations
def p_declarationList(p):
    """
    declarationList : declaration
                    | declaration declarationList
    """
    pass
    # if len(p) == 2:
    #     p[0] = Node("declaration-list", None, None, [p[1]])
    # else:
    #     p[0] = Node("declaration-list", None, None, [p[1], p[2]])

# Rule to implement single declaration
def p_declaration(p):
    """
    declaration : varDeclaration
                | constDeclaration
                | staticDeclaration
                | funcDeclaration
    """
    pass
    # p[0] = Node("declaration", None, None, [p[1]])

# Rule to implement variable declaration
def p_varDeclaration(p):
    """
    varDeclaration : LET IDVAR EQUAL IDVAR SEMCL
                   | LET IDVAR EQUAL INTVR SEMCL
                   | LET IDVAR EQUAL STRNG SEMCL
                   | LET IDVAR EQUAL expression SEMCL
    """
    pass
    # if len(p) == 6:
    #     p[0] = Node('varDeclaration', [p[2], p[2]], None, None)
    # else:
    #     p[0] = Node('varDeclaration', [p[2]], None, None)

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
    pass
    # T = Node("FN")
    # p[0] = Node("function-declaration", None, None, [T, p[2]])

# Rule to implement functions
def p_function(p):
    """
    function : FN parameters block
    """
    pass
    # T = Node("FN", p[1])
    # p[0] = Node("function", None, None, [T, p[2], p[3]])

# Rule to implement parameters for functions
def p_parameters(p):
    """
    parameters : OPENP CLOSP
               | OPENP paramList CLOSP
    """
    pass
    # T1 = Node("OPENP", p[1])
    # if (len(p) == 3):  # First case
    #     T2 = Node("CLOSP", p[2])
    #     p[0] = Node("parameters", None, None, [T1, T2])
    # else:
    #     T2 = Node("RPAREN", p[3])
    #     p[0] = Node("parameters", None, None, [T1, T2, p[2]])

# Rule to implement parameter list
def p_paramList(p):
    """
    paramList : parameter
              | parameter COMMA paramList
    """
    pass
    # if len(p) == 2:
    #     p[0] = Node('parameter-list', None, None, [p[1]])
    # else:
    #     T = Node('COMMA', p[2])
    #     p[0] = Node('parameter-list', None, None, [p[1], T, p[3]])

# Rule for general parameters
def p_parameter(p):
    """
    parameter : IDVAR
    """
    pass
    # T = Node('IDVAR', p[1])
    # p[0] = Node('parameter', None, None, [T])

# Rule for block of code
def p_block(p):
    """
    block : LBCKT RBCKT
          | LBCKT statement-list RBCKT
    """
    pass
    # T1 = Node("LBCKT", p[1])
    #
    # if (len(p) == 3):  # First case
    #     T2 = Node("RBCKT", p[2])
    #     p[0] = Node("block", None, None, [T1, T2])
    # else:
    #     T2 = Node("RBCKT", p[3])
    #     p[0] = Node("block", None, None, [T1, T2, p[2]])

# Rule for statement list
def p_statement_list(p):
    """
    statement-list : stmt
                   | stmt statement-list
    """
    pass
    # if len(p) == 2:
    #     p[0] = Node('statement-list', None, None, [p[1]])
    # else:
    #     p[0] = Node('statement-list', None, None, [p[1], p[2]])

# Rule to implement statements
def p_stmt(p):
    """
    stmt : expression
         | declaration
         | selectionStmt
         | iterationStmt
         | inputStmt
         | outputStmt
    """
    pass
    # p[0] = Node('stmt', None, None, [p[1]])

# Rule to implement expressions
def p_expression(p):
    """
    expression : basicExp
               | assignmentExp SEMCL
               | comparisonExp
    """
    pass
    # p[0] = Node('expression', None, None, [p[1]])

# Rule for basic expressions
def p_basic(p):
    """
    basicExp : IDVAR
             | INTVR
             | STRNG
    """
    pass
    # v = Node('BASIC', p[1])
    # p[0] = Node('basicExp', None, None, [v])

# Rule for general variables
def p_id(p):
    """
    identifier : IDVAR
               | INTVR
    """
    pass
    # T = Node('ID', p[1])
    # p[0] = Node('intvariable', None, None, [T])

# Rule to implement assignment expressions
def p_assignment_expression(p):
    """
    assignmentExp : identifier sumOp basicExp
                  | identifier sumOp assignmentExp
    """
    pass
    # if len(p) == 4:
    #     p[0] = Node('assignment-expr', None, None, [p[1], p[2], p[3]])
    # else:
    #     p[0] = Node('assignment-expr', None, None, [p[1], p[2]])

# Rule to implement comparison expressions
def p_compExp(p):
    """
    comparisonExp : basicExp relop basicExp
                  | basicExp relop comparisonExp
    """
    pass
    # p[0] = Node('comparisonExp', None, None, [p[1], p[2], p[3]])

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
    # T = Node(p[1], p[1])
    # p[0] = Node('relop', None, None, [T])

# Rule for arithmetic operators
def p_sumOp(p):
    """
    sumOp : ADDOP
          | SUBOP
          | DEROP
          | QUOOP
          | EQUAL
    """
    pass
    # T = Node(p[1], p[1])
    # p[0] = Node('sumOp', None, None, [T])

# Rule to implement if statements
def p_selectionStmt(p):
    """
    selectionStmt : IF expression EQUAL block
                  | IF expression EQUAL block ELSE
    """
    pass
    # T = Node('IF', p[1])
    # p[0] = Node('selectionStmt', None, None, [T, p[3], p[5]])

# Rule to implement iterations
def p_iterationStmt(p):
    """
    iterationStmt : FOR basicExp IN expression
                  | WHILE basicExp EQLTO expression
                  | WHILE basicExp LESST expression
                  | WHILE basicExp GREAT expression
    """
    pass
    # T = Node('FOR', p[1])
    # p[0] = Node('iterationStmt', None, None, [T, p[2], p[3]])

# # Rule for general expression
# def p_expression(p):
#     """
#     expression : expression OROPE expression
#     """
#     pass
#     # p[0] = Node('expression', None, None, [p[1]])

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

# # Rule for booleans
# def p_booleans(p):
#     """
#     booleans : LET IDVAR EQUAL TRUE
#              | LET IDVAR EQUAL FALSE
#     """
#     pass

# Rule for Catastrophic error
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Import yacc
import ply.yacc as yacc
parser = yacc.yacc(start='foo')
