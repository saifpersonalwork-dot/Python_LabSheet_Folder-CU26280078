"""Lab solution: Flatten Nested List
Question number: 09
"""

import ast
nested = ast.literal_eval(input("Enter nested list, e.g. [[1, 2], [3, [4]]]: "))
def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list): result.extend(flatten(item))
        else: result.append(item)
    return result
print(flatten(nested))
