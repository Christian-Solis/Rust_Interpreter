# -----------------------------------------------------------------------------
# Parser Tests
# -----------------------------------------------------------------------------

from rust_parser import *

# Success
# Variable definition
TestNo1 = '''
let FIVE = 5
'''

# Constants definition
TestNo2 = '''
static NINE = 9
const TEN = 10
'''

# Loop and conditional
TestNo3 = '''
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

# Input and output
TestNo4 = '''
for line in stdin {
}
println!("I just printed this!");
'''

# All the rules
TestNo5 = '''
while FIVE > 5:
    stdin()
    println!("Yes")
    FIVE = FIVE - 1
    if FIVE == 3:
        print("FIVE is now 3")
    else:
        print("Value is not 3");
'''

# Failure
# Variable definition on the wrong place
TestNo6 = '''
"chris" let = crsc
'''

# Using a string in a not allowed way
TestNo7 = '''
"Esto es un string" = si;
'''

# Loop with wrong wrammar
TestNo8 = '''
while:
    print("No")
'''

# Incorrect inputs but with success for now
TestNo9 = '''
x = 5
x = "String"
'''

# Method using a class that does not contain such a method
TestNo10 = '''
x.method1().method2()
'''

# Variable outside the scope
TestNo11 = '''
def function1(): variable2 = 2; variable2 x;
variable2;
'''

# -----------------------------------------------------------------------------
# Running of Tests
# -----------------------------------------------------------------------------

# Run Tests
print("\n Test 1:")
yacc.parse(TestNo1)

print("\n Test 2:")
yacc.parse(TestNo2)

print("\n Test 3:")
yacc.parse(TestNo3)

print("\n Test 4:")
yacc.parse(TestNo4)

print("\n Test 5:")
yacc.parse(TestNo5)

print("\n Test 6:")
yacc.parse(TestNo6)

print("\n Test 7:")
yacc.parse(TestNo7)

print("\n Test 8:")
yacc.parse(TestNo8)

print("\n Test 9:")
yacc.parse(TestNo9)

print("\n Test 10:")
yacc.parse(TestNo10)

print("\n Test 11:")
yacc.parse(TestNo11)
