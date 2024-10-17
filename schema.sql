use zeotap;
show tables;

select * from rule_nodes;
desc rule_nodes;
select * from rules;
INSERT INTO rules (rule_name)
VALUES ('Eligibility Rule 1');

INSERT INTO rule_nodes (rule_id, node_type,operand_value)
VALUES (1, 'operand', 'age > 30');  
INSERT INTO rule_nodes (rule_id, node_type,operand_value)
VALUES (1, 'operand', 'department == ''Sales''');  -- ID 2


INSERT INTO rule_nodes (rule_id, node_type, operand_value, left_child_id, right_child_id)
VALUES (1, 'operator', 'AND', 1, 2);  -- ID 3 (left_node_id = 1, right_node_id = 2)

-- Insert operands
INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (1, 'operand', 'age > 30');  -- ID 4
INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (1, 'operand', 'department == ''Sales''');  -- ID 5
INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (1, 'operand', 'age < 25');  -- ID 6
INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (1, 'operand', 'department == ''Marketing''');  -- ID 7
INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (1, 'operand', 'salary > 50000');  -- ID 8
INSERT INTO rule_nodes (rule_id, node_type, operand_value) VALUES (1, 'operand', 'experience > 5');  -- ID 9

-- Insert operators
INSERT INTO rule_nodes (rule_id, node_type, operand_value, left_child_id, right_child_id) VALUES (1, 'operator', 'AND', 4, 5);  -- ID 10 (age > 30 AND department == 'Sales')
INSERT INTO rule_nodes (rule_id, node_type, operand_value, left_child_id, right_child_id) VALUES (1, 'operator', 'AND', 6, 7);  -- ID 11 (age < 25 AND department == 'Marketing')
INSERT INTO rule_nodes (rule_id, node_type, operand_value, left_child_id, right_child_id) VALUES (1, 'operator', 'OR', 10, 11);  -- ID 12 (Combine with OR)
INSERT INTO rule_nodes (rule_id, node_type, operand_value, left_child_id, right_child_id) VALUES (1, 'operator', 'OR', 8, 9);  -- ID 13 (salary > 50000 OR experience > 5)
INSERT INTO rule_nodes (rule_id, node_type, operand_value, left_child_id, right_child_id) VALUES (1, 'operator', 'AND', 12, 13);  -- ID 14 (Final AND)










