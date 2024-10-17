from node import Node

def create_rule(rule_string):
    # Tokenize and parse the string to create the AST
    # Example hardcoded for demo
    root = Node("operator", value="AND")
    root.left = Node("operator", value="OR")
    root.left.left = Node("operand", value="age > 30 AND department == 'Sales'")
    root.left.right = Node("operand", value="age < 25 AND department == 'Marketing'")
    root.right = Node("operator", value="OR")
    root.right.left = Node("operand", value="salary > 50000")
    root.right.right = Node("operand", value="experience > 5")
    
    return root
