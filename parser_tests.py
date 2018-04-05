# -----------------------------------------------------------------------------
# Parser Tests
# -----------------------------------------------------------------------------

'''
# One word comment
TestNo1 = '''
// This
'''

from parser import *




# Success
# Variable definition
'''
let FIVE = 5;
'''

# Constants definition
'''
static NINE = 9;
const TEN = 10;
'''

# Loop and conditional
'''
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
'''
for line in stdin {
}
println!("I just printed this!");
'''

# All the rules
'''
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
'''
"chris" let = crsc
'''

# Using a string in a not allowed way
'''
"Esto es un string" = si;
'''

# Loop with wrong wrammar
'''
while:
    print("No")
'''

# Incorrect inputs but with success for now
'''
x = 5
x = "String"
'''

# Method using a class that does not contain such a method
'''
x.method1().method2()
'''

# Variable outside the scope
'''
def function1(): variable2 = 2; variable2 x;
variable2;
'''
