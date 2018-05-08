# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés
# A01063685
# Compilers Design
# Parser Specification of Project:
# Rust interpreter with Python
# AST
# -----------------------------------------------------------------------------

class SymbolTable:

    def __init__(self):
        self.symbol_table = []
        self.symbol_table.append(dict())
        self.scope = 0

    def __str__(self):
        return "{0}".format(self.symbol_table)

    def add_object(self, key, new_obj):
        self.symbol_table[self.scope]
        self.symbol_table[self.scope][key] = dict()
        self.symbol_table[self.scope][key]["val"] = new_obj
        self.symbol_table[self.scope][key]["type"] = type(new_obj)
        # print(self.symbol_table)

    def get_object_val(self, key):
        scope = self.scope
        while scope > 0 and not key in self.symbol_table[scope]:
            scope -= 1
        if scope == -1:
            print("Undefined name '%s'" % key)
            return 0
        try:
            return self.symbol_table[scope][key]["val"]
        except LookupError:
            print("Undefined name '%s'" % key)
            return 0

    def increase_scope(self):
        self.scope += 1
        self.symbol_table.append(dict())
        # print("increase: {0}".format(self.symbol_table))

    def decrease_scope(self):
        self.scope -= 1
        self.symbol_table.pop()
        # print("decrease: {0}".format(self.symbol_table))

    def delete_scoped_variables(self, scope):
        while self.scope > scope:
            self.decrease_scope()


symbol_table = SymbolTable()
