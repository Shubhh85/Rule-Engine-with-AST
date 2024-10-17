def evaluate_rule(node, data):
    if node.node_type == "operand":
        return eval(node.value, {}, data)
    elif node.node_type == "operator":
        if node.value == "and":
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == "or":
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
    return False
