# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Compilers Design
# Lexical Specification of Project:
# Rust interpreter with Python
# -----------------------------------------------------------------------------



# Reserved words
# 'reserved word' :'given name'
reserved = {
    'let' : 'LET',
    'static' : 'STATIC',
    'const' : 'CONST',
    'stdin' : 'STDIN',
    'println!' : 'PRINTLN',
    'iter' : 'ITER',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'concat' : 'CONCAT',
    'String' : 'STRING',
    'new' : 'NEW',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'loop' : 'LOOP',
    'while' : 'WHILE',
    'for' : 'FOR',
    'in' : 'IN',
}

tokens = list(reserved.values()) + [
    'DOTOP',
    'LOOPC','WHILE','FORCN','INCON',
    'ADDOP','SUBOP','QUOOP','DEROP','REMOP',
    'ANDOP','OROPE','EQUAL','EQLTO','UNEQL',
    'LESST','GREAT','LSSEQ','GRTEQ',
    #'SCOPE',
    'STRNG',
    'SLCOM','BLCOM',
    'IDVAR','INTVR',
    'OPENP','CLOSP',
    'LBCKT','RBCKT',
    'SEMCL',
    ]

# Tokens
t_DOTOP = r'\.'
t_ADDOP = r'\+'
t_SUBOP = r'-'
t_QUOOP = r'/'
t_DEROP = r'\*'
t_REMOP = r'%'
t_ANDOP = r'&'
t_OROPE = r'\|\|'
t_EQUAL = r'='
t_EQLTO = r'\=\='
t_UNEQL = r'\=\!'
t_LESST = r'<'
t_GREAT = r'>'
t_LSSEQ = r'\<\='
t_GRTEQ = r'\>\='
#t_SCOPE = r'\[::]'
t_STRNG = r'"[ a-zA-Z_][ a-zA-Z0-9_][ a-zA-Z0-9_~?!@#$%^&-]*"'
t_INTVR = r'[-+]?[0-9]+'
t_OPENP = r'\('
t_CLOSP = r'\)'
t_LBCKT = r'{'
t_RBCKT = r'}'
t_SEMCL = r';'

# -----------------------------------------------------------------------------
# Rules
# -----------------------------------------------------------------------------

# Rule for ID's
def t_IDVAR(t):
    r'[a-zA-Z_!.][a-zA-Z0-9_!.]*'
    #r'[a-zA-Z_:.][a-zA-Z_:0-9]*'
    # Look up symbol table information and return a tuple
    #t.value = (t.value, symbol_lookup(t.value))
    # Check for reserved words
    t.type = reserved.get(t.value,'IDVAR')
    return t

# Ignored characters
t_ignore = " \t"

# Rule for new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Stop when finding an error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    # skip ahead one character by calling t.lexer.skip(1)
    t.lexer.skip(1)

# Rule to discard single line comments
def t_SLCOM(t):
    r'//.*' # This ok?
    # No return value. Token discarded
    pass

# Rule to discard single line comments
def t_BLCOM(t):
    r'///(.|\n)?///'
    # No return value. Token discarded
    pass

# Compute column for error handling
#   input is the input text string
#   token is a token instance
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
	       last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# dictionary of names (for storing variables)
# names = { }

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Build the yacc
# import ply.yacc as yacc
# yacc.yacc()

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------

# One word comment
TestNo1 = '''
// This
'''

# One line comment
TestNo2 = '''
// This is a line comment
'''

# Variable definition
TestNo3 = '''
let FIVE = 5;
'''

# Constants definition
TestNo4 = '''
static NINE = 9;
const TEN = 10;
'''

# String definition
TestNo5 = '''
let string = "This is a string";
'''

# Data types definition
TestNo6 = '''
let x = 5;
let string = "This is a string";
let chris = true;
'''

# Data types definition
TestNo6 = '''
let x = 5;
let string = "This is a string";
let chris = true;
'''

# Loop and Conditional definition
TestNo7 = '''
for var in expression {
    code
}
if n < 10 {
 code
}
else {
 code
}
'''

# Input and Output definition
TestNo8 = '''
for line in stdin {
}
println!("I just printed this!");
'''

# Mix of all instructions
TestNo9 = '''
// This
// This is a line comment

let x = 5;
let string = "This is a string";
let chris = true;
static NINE = 9;
const TEN = 10;

for var in expression {
    for var in expression{
        code
    }
}
if n < 10 {
 code
}
else {
 code
}

for line in stdin {
}
println!("I just printed this!");
'''

# -----------------------------------------------------------------------------
# Extra Tests
# -----------------------------------------------------------------------------

# Variable definition on the wrong place
ExtraTestNo1 = '''
"chris" let = crsc
'''

# String, variable and constant on a place that is not allowed
ExtraTestNo2 = '''
const "my name" = let christian
'''

# loop defined using a wrong grammar
ExtraTestNo3 = '''
for var in expression {
    12bc = 3

    °¬¬~~
}
'''

# -----------------------------------------------------------------------------
# Running of Tests
# -----------------------------------------------------------------------------

# Run Tests
print("\n Test 1 Single Word Comment:")
lex.runmain(data = TestNo1)

print("\n Test 2 Single Line Comment:")
lex.runmain(data = TestNo2)

print("\n Test 3 Variable Definition:")
lex.runmain(data = TestNo3)

print("\n Test 4 Constants Definition:")
lex.runmain(data = TestNo4)

print("\n Test 5 String Definition:")
lex.runmain(data = TestNo5)

print("\n Test 6 Data Types Definition:")
lex.runmain(data = TestNo6)

print("\n Test 7 Loop and Conditional Definition:")
lex.runmain(data = TestNo7)

print("\n Test 8 Input and Output Definition:")
lex.runmain(data = TestNo8)

print("\n Test 9 Mix of All Instructions:")
lex.runmain(data = TestNo9)

print("\n Extra Tests:")

print("\n Test 1 Variable Definition on the Wrong Place:")
lex.runmain(data = ExtraTestNo1)

print("\n Test 2 Variable Definition on the Wrong Place:")
lex.runmain(data = ExtraTestNo2)

print("\n Test 3 Variable Definition on the Wrong Place:")
lex.runmain(data = ExtraTestNo3)

#while True:
#    try:
#        s = input('Interpreter Rust (^-^) ')
#    except EOFError:
#        break
#    lexer.input(s)
#    for token in lexer:
#        print(token)
