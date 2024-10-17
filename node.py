class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" for AND/OR, "operand" for conditions
        self.left = left  # Reference to left child node
        self.right = right  # Reference to right child node
        self.value = value  # Operator value (AND/OR) or condition value

    def __repr__(self):
        if self.node_type == "operator":
            return f"({self.left} {self.value} {self.right})"
        elif self.node_type == "operand":
            return f"{self.value}"
