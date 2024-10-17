import mysql.connector
from node import Node

def insert_rule(rule_name, ast_root):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zeotap"
    )
    cursor = connection.cursor()

    cursor.execute("INSERT INTO rules (rule_name) VALUES (%s)", (rule_name,))
    rule_id = cursor.lastrowid

    def insert_node(node, rule_id):
        if node.node_type == 'operator':
            cursor.execute(
                "INSERT INTO rule_nodes (rule_id, node_type, operator_value) VALUES (%s, %s, %s)",
                (rule_id, 'operator', node.value)
            )
        elif node.node_type == 'operand':
            cursor.execute(
                "INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (%s, %s, %s)",
                (rule_id, 'operand', node.value)
            )
        node_id = cursor.lastrowid

        if node.left:
            left_child_id = insert_node(node.left, rule_id)
            cursor.execute("UPDATE rule_nodes SET left_child_id = %s WHERE node_id = %s", (left_child_id, node_id))
        if node.right:
            right_child_id = insert_node(node.right, rule_id)
            cursor.execute("UPDATE rule_nodes SET right_child_id = %s WHERE node_id = %s", (right_child_id, node_id))

        return node_id

    insert_node(ast_root, rule_id)

    connection.commit()
    cursor.close()
    connection.close()

def fetch_rule(rule_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zeotap"
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM rule_nodes WHERE rule_id = %s", (rule_id,))
    nodes = cursor.fetchall()

    node_dict = {}
    for node in nodes:
        node_dict[node['node_id']] = Node(node_type=node['node_type'],
                                          value=node['operator_value'] if node['node_type'] == 'operator' else node['operand_value'])

    for node in nodes:
        if node['left_child_id']:
            node_dict[node['node_id']].left = node_dict[node['left_child_id']]
        if node['right_child_id']:
            node_dict[node['node_id']].right = node_dict[node['right_child_id']]

    root_node = node_dict[nodes[0]['node_id']]
    cursor.close()
    connection.close()
    
    return root_node
