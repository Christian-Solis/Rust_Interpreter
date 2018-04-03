# Node class structure to handle nodes
class Node:
    def __init__(self, token, value=None, node_type=None, children=None):
        self.token = token
        self.value = value
        self.node_type = ntype
        # If a children exists
        if children:
            self.children = children
        else:
            self.children = []

    # Get the values of the nodes
    def get_node_values(self):
        return '"' + self.token + ':' + str(self.value) + ':' + \
                str(self.node_type) + '"'

    # Return the valies
    def print_node(self):

        if self.children:
            for child in self.children:
                print(self.get_node_values(), '->', child.get_node_values())
                child.print_node()
