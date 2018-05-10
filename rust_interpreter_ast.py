# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Compilers Design
# Parser Specification of Project:
# Rust interpreter with Python
# AST
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Symble table will be a list of dictionaries
# -----------------------------------------------------------------------------

class SymbolTable:

    def __init__(self):
        # Empty list
        self.symbol_table = []
        # Add dictionary to the list
        self.symbol_table.append(dict())
        # Initial scope 0
        self.scope = 0

    def __str__(self):
        return "{0}".format(self.symbol_table)

    # Add object to the SymbleTable class
    def append_object(self, key, new_object):
        self.symbol_table[self.scope]
        self.symbol_table[self.scope][key] = dict()
        self.symbol_table[self.scope][key]["value"] = new_object
        self.symbol_table[self.scope][key]["type"] = type(new_object)
        # print(self.symbol_table)

    # Get the value of the object
    def get_object_value(self, key):
        scope = self.scope
        while scope > 0 and not key in self.symbol_table[scope]:
            scope -= 1
        if scope == -1:
            # If key is not in the SymbleTable
            print("Not defined name '%s'" % key)
            return 0
        try:
            return self.symbol_table[scope][key]["value"]
        except LookupError:
            print("Not defined name '%s'" % key)
            return 0

    # Scope of the table +1
    def increase_scope(self):
        self.scope += 1
        self.symbol_table.append(dict())

    # Scope of the table -1
    def decrease_scope(self):
        self.scope -= 1
        self.symbol_table.pop()

    # Calling of decrease_scope
    def delete_scoped_variables(self, scope):
        while self.scope > scope:
            self.decrease_scope()

the_symbol_table = SymbolTable()

class Node(object):
    # execute function
    def execute(self):
        raise NotImplementedError("Not abstract method implemented")

# Rule to run program
class p_program(Node):
    """
    program : declarationList
            | statementList
    """
    def __init__(self, program, program1=None):
        self.program = program
        # self.declarationList = declarationList
        # self.statementList = statementList

    def execute(self):
        self.program.execute()
        if self.program:
            self.program.execute()


# Rule to implement several declarations
class p_declarationList(Node):
    """
    declarationList : declaration
                    | declaration declarationList
    """
    def __init__(self, declarationList):
        self.declarationList = declarationList
        # self.declaration = declaration

    def execute(self):
        self.declarationList.execute()

# Rule to implement single declaration
class p_declaration(Node):
    """
    declaration : varDeclaration
                | constDeclaration
                | staticDeclaration
                | funcDeclaration
    """
    def __init__(self, declaration):
        self.declaration = declaration

    def execute(self):
        return self.declaration.execute()

# Rule to implement variable declaration
class p_varDeclaration(Node):
    """
    varDeclaration : LET IDVAR EQUAL expression SEMCL
                   | LET IDVAR EQUAL identifier SEMCL
    """
    def __init__(self, LET, IDVAR, EQUAL, expression, SEMCL):
        self.let = LET
        self.idvar = IDVAR
        self.equal = EQUAL
        self.expression = expression
        self.semcl = SEMCL

    def execute(self):
        if str(self.expression)[0] == "'" or str(self.expression)[0] == '"':
            symbol_table.add_object(str(self.idvar), self.expression)
            return self.expression
        else:
            value = self.expression.execute()
            symbol_table.add_object(str(self.idvar), value)
            return value

# Rule to implement constant declaration
class p_constDeclaration(Node):
    """
    constDeclaration : CONST IDVAR EQUAL expression SEMCL
    """
    def __init__(self, CONST, IDVAR, EQUAL, expression, SEMCL):
        self.const = CONST
        self.idvar = IDVAR
        self.equal = EQUAL
        self.expression = expression
        self.semcl = SEMCL
    def execute(self):
        if str(self.expression)[0] == "'" or str(self.expression)[0] == '"':
            symbol_table.add_object(str(self.idvar), self.expression)
            return self.expression
        else:
            value = self.expression.execute()
            symbol_table.add_object(str(self.idvar), value)
            return value


# Rule to implement static declaration
class p_staticDeclaration(Node):
    """
    staticDeclaration : STATIC IDVAR EQUAL expression SEMCL
    """
    def __init__(self, STAIC, IDVAR, EQUAL, expression, SEMCL):
        self.const = CONST
        self.idvar = IDVAR
        self.equal = EQUAL
        self.expression = expression
        self.semcl = SEMCL
    def execute(self):
        if str(self.expression)[0] == "'" or str(self.expression)[0] == '"':
            symbol_table.add_object(str(self.idvar), self.expression)
            return self.expression
        else:
            value = self.expression.execute()
            symbol_table.add_object(str(self.idvar), value)
            return value

# Rule to implement function declarations
class p_funcDeclaration(Node):
    """
    funcDeclaration : FN function
    """
    pass

# Rule to implement functions
class p_function(Node):
    """
    function : IDVAR parameters block
    """
    pass

# Rule to implement parameters for functions
class p_parameters(Node):
    """
    parameters : OPENP CLOSP
               | OPENP paramList CLOSP
               | OPENP expression CLOSP
    """

# Rule to implement parameter list
class p_paramList(Node):
    """
    paramList : parameter
              | parameter COMMA paramList
    """
    pass

# Rule for general parameters
class p_parameter(Node):
    """
    parameter : IDVAR
              | INTVR
              | STRNG
    """
    pass

# Rule for block of code
class p_block(Node):
    """
    block : LBCKT RBCKT
          | LBCKT statement-list RBCKT
    """
    pass


# Rule for statement list
class p_statement_list(Node):
    """
    statement-list : stmt
                   | stmt statement-list
    """
    pass

# Rule for inputs
class p_input_stmt(Node):
    """
    inputStmt : STDIN OPENP stmt CLOSP SEMCL
    """
    def __init__(self):
        self.type = 'STDIN'

    def execute(self):
        return input()

# Rule for outputs
class p_output_stmt(Node):
    """
    outputStmt : PRINTLN OPENP stmt CLOSP SEMCL
    """
    def __init__(self):
        self.type = 'PRINTLN'

    def execute(self):
        return println()

# Rule to implement statements
class p_stmt(Node):
    """
    stmt : expression
         | declaration
         | selectionStmt
         | iterationStmt
         | inputStmt
         | outputStmt
    """
    def __init__(self, stmt):
        self.stmt = stmt

    def execute(self):
        self.stmt.execute()

# Rule to implement expressions
class p_expression(Node):
    """
    expression : basicExp
               | assignmentExp SEMCL
               | comparisonExp
               | boolExp
    """
    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        self.stmt.execute()

# Rule for basic expressions
class p_basic(Node):
    """
    basicExp : INTVR
             | STRNG
             | IDVAR
    """
    pass

# Rule to implement assignment expressions
class p_assignment_expression(Node):
    """
    assignmentExp : identifier sumOp basicExp
                  | identifier sumOp assignmentExp
    """
    pass
    def __init__(self, identifier, sumop, basicExp):
        self.identifier = identifier
        self.sumop = sumop
        self.basicExp = basicExp

    def execute(self):
        if self.sumop:
            if self.sumop.execute() == '+': return self.identifier.execute() + self.basicExp.execute()
            elif self.sumop.execute() == '-': return self.identifier.execute() - self.basicExp.execute()
        else:
            return self.basicExp.execute()

# Rule for general variables
class p_id(Node):
    """
    identifier : IDVAR
               | INTVR
    """
    pass

# Rule to implement comparison expressions
class p_compExp(Node):
    """
    comparisonExp : basicExp relop basicExp
                  | basicExp relop comparisonExp
    """
    pass

# Rule for operators
class p_relop(Node):
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

# Rule for arithmetic operators
class p_sumOp(Node):
    """
    sumOp : ADDOP
          | SUBOP
          | DEROP
          | QUOOP
          | EQUAL
          | REMOP
    """
    pass

# Rule to implement if statements
class p_selectionStmt(Node):
    """
    selectionStmt : IF OPENP expression CLOSP block
                  | IF OPENP expression CLOSP block ELSE block
    """
    pass

# Rule to implement iterations
class p_iterationStmt(Node):
    """
    iterationStmt : FOR expression IN expression
                  | WHILE parameters block
    """
    pass
    # def __init__(self, FOR, expression, IN, expression, SEMCL):
    #     self.forloop = FOR
    #     self.expression = expression
    #     self.inloop = IN
    #
    # def execute(self):
    #     symbol_table.increase_scope()
    #     while self.expression.execute():
    #         self.expression.execute()

class p_boolExp(Node):
    """
    boolExp : TRUE
            | FALSE
    """
    pass
