from rule_creator import create_rule
from db_functions import insert_rule, fetch_rule
from rule_evaluator import evaluate_rule

# Create and insert a rule
rule_ast = create_rule("((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)")
insert_rule("Eligibility Rule 1", rule_ast)

# Fetch and evaluate the rule
rule_ast = fetch_rule(1)  # Fetch rule with ID 1
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(rule_ast, data)

print(result)  # Expected output: True
