# -----------------------------------------------------------------------------
# Lexer Tests
# -----------------------------------------------------------------------------

'''
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
'''
